import unittest
import time
import csv
import importlib.util
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver as OriginalChrome
from concurrent.futures import ProcessPoolExecutor, as_completed

#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
project = "prestashop"
base_dir = Path(r"C:\Diana\MasterCode\code\Projects")
collected_dir = base_dir / project / "Processes" / "collectedSuccessGEMINI"
results_dir = Path(r"C:\Diana\MasterCode\code\Documantation")
results_dir.mkdir(parents=True, exist_ok=True)
csv_file = results_dir / f"mutation_report_FIN.csv"
timestamp = time.strftime("%Y%m%d_%H%M%S")

pre_mutation = False
repeat_runs = 1
current_mutation = {
    #"type": "RENAME",
    #"type": "REMOVE1",
    "type": "REMOVE2",
    #"description": "Renamed buttons - add to cart, sign in, register, account and store button",
    #"description": "Removed add to cart button and filter buttons",
    "description": "Removed checkout button and filter at all",
    #"expected": "pass"
    "expected": "fail"
}

def append_to_csv(project, model_name, prompt_type, resolution, run_id,
                  test_module, status, exec_time, total_tests, total_time,
                  mutation_type="", mutation_description="", expected_result="", match="",
                  repeat_num=1):
    file_exists = csv_file.is_file()
    with csv_file.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "Timestamp", "Project", "Model", "PromptType", "Resolution",
                "RunID", "TestModule", "Repeat", "Status", "ExecutionTime(sec)", "TotalTests", "TotalTime(sec)",
                "MutationType", "MutationDescription", "ExpectedResult", "Match"
            ])
        writer.writerow([
            timestamp, project, model_name, prompt_type, resolution,
            run_id, test_module, repeat_num, status, exec_time, total_tests, total_time,
            mutation_type, mutation_description, expected_result, match
        ])

def headless_chrome(*args, **kwargs):
    options = kwargs.get("options", Options())
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    kwargs["options"] = options
    return OriginalChrome(*args, **kwargs)

webdriver.Chrome = headless_chrome

def execute_test(args):
    project, model_name, prompt_type, resolution, run_id, module_name, module_path, total_tests = args
    total_start = time.time()
    try:
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        suite = unittest.TestLoader().loadTestsFromModule(module)
        start = time.time()
        result = unittest.TextTestRunner(verbosity=0).run(suite)
        end = time.time()
        elapsed = round(end - start, 2)
        if result.wasSuccessful():
            status = "pass"
        elif result.errors:
            status = "error"
        elif result.failures:
            status = "fail"
        else:
            status = "unknown"

    except Exception as e:
        status = "load_error"
        elapsed = 0
        print(f"ERROR: {module_name}: {str(e)}")

    if not pre_mutation:
        mutation_type = current_mutation.get("type", "")
        mutation_description = current_mutation.get("description", "")
        expected_result = current_mutation.get("expected", "")
        if expected_result == "fail" and status in ["fail", "error"]:
            match = "Matched"
        elif status == expected_result:
            match = "Matched"
        else:
            match = "Mismatch"
    else:
        mutation_type = mutation_description = expected_result = match = ""
    append_to_csv(
        project, model_name, prompt_type, resolution, run_id,
        module_name, status, elapsed, total_tests, round(time.time() - total_start, 2),
        mutation_type, mutation_description, expected_result, match
    )

all_files = [f for f in collected_dir.iterdir() if f.suffix == ".py"]
for repeat_num in range(1, repeat_runs + 1):
    all_tasks = []
    for file in all_files:
        try:
            parts = file.stem.split("__")
            if len(parts) == 6:
                model_name, prompt_type, resolution, run_id, mode, test_module = parts
            elif len(parts) == 5:
                model_name, prompt_type, run_id, mode, test_module = parts
                resolution = "NO"
            module_path = file
            all_tasks.append((
                project, model_name, prompt_type, resolution, run_id,
                test_module, module_path, 1
            ))
        except Exception as e:
            print(f"ERROR: {file.name} → {e}")
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(execute_test, task) for task in all_tasks]
        for future in as_completed(futures):
            _ = future.result()

print(f"FIN - REPORT: {csv_file}")
