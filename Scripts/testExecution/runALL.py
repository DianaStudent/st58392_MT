
import csv
import time
import unittest
import importlib.util
import pandas as pd
from pathlib import Path
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ProcessPoolExecutor, as_completed

import step_counter_patch  

base_dir = Path(r"C:\diana\MasterCode\code\projects")
#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
projects = ["medusa"]
sources = [("tests", "tests"), ("testsURLchange", "testsURLchange"), ("testsDriverChange", "testsDriverChange"), ("failed", "failed")]
output_csv = Path(r"C:\diana\MasterCode\code\Documantation\reports\manualcheck\updatedTestsResults\URL\all_fin.csv")
alt_csv = Path(r"C:\diana\MasterCode\code\Documantation\reports\manualcheck\updatedTestsResults\URL\all_fulldump_fin.csv")
timestamp = time.strftime("%Y%m%d_%H%M%S")
_original_chrome = webdriver.Chrome
def headless_chrome(*args, **kwargs):
    if args:
        executable_path = args[0]
        args = args[1:]
    else:
        executable_path = kwargs.pop("executable_path", None)
    options = kwargs.get("options", Options())
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    kwargs["options"] = options
    return _original_chrome(executable_path, *args, **kwargs) if executable_path else _original_chrome(*args, **kwargs)
webdriver.Chrome = headless_chrome

resolution_readable = {
    "1024": "1024x1024",
    "768": "768x768",
    "source": "1920x893",
    "672": "672x672",
    "NO": "No screenshot"
}

model_readable = {
    "gpt4o": "GPT-4o",
    "gpt4oHTML": "GPT-4o (only HTML)",
    "llava-llama3": "LLaVA-LLaMA3",
    "llava-llamav3": "LLaVA-LLaMA3",
    "llava-llamav3HTML": "LLaVA-LLaMA3 (only HTML)",
    "llava7bllama3.1.8b": "LLaVA:7b combined with LLaMA3.1:8b",
    "llava7bllama3.1.8bHTML": "LLaMA3.1:8b (only HTML)"
}

readable_mapping = {
    ("process", "test_login"): "Authorization process",
    ("process", "test_register"): "Registration process",
    ("process", "test_filter"): "Application of filters process",
    ("process", "test_addtocart"): "Add to cart process",
    ("process", "test_checkout"): "Checkout process",
    ("ui", "test_home"): "Home page",
    ("ui", "test_login"): "Login page",
    ("ui", "test_login_page"): "Login page",
    ("ui", "test_register"): "Registration page",
    ("ui", "test_register_page"): "Registration page",
    ("ui", "test_search_page"): "Search page",
    ("ui", "test_category_a_1"): "Product pages",
    ("ui", "test_category_a"): "Product pages",
    ("ui", "test_chairs"): "Product pages",
    ("ui", "test_tables"): "Product pages",
    ("ui", "test_accessories"): "Product pages",
    ("ui", "test_art"): "Product pages",
    ("ui", "test_clothes"): "Product pages",
    ("ui", "test_UI"): "Home page"
}

def classify_error(msg):
    if pd.isna(msg):
        return "OK"
    msg = msg.lower()
    if "element not interactable" in msg:
        return "ElementNotInteractable"
    if "element click intercepted" in msg:
        return "ClickIntercepted"
    if "name 'html_data' is not defined" in msg:
        return "HtmlDataUndefined"
    if "invalid argument" in msg:
        return "InvalidURL"
    if "connection refused" in msg or "err_connection_refused" in msg:
        return "ConnectionRefused"
    if "err_name_not_resolved" in msg:
        return "NameNotResolved"
    if "session not created" in msg:
        return "SessionNotCreated"
    if "syntaxerror" in msg:
        return "SyntaxError"
    if "assertionerror" in msg:
        return "AssertionError"
    if "no such element" in msg:
        return "NoSuchElement"
    if "timeoutexception" in msg:
        return "Timeout"
    if "typeerror" in msg:
        return "TypeError"
    if "webdriverexception" in msg:
        return "WebDriverException"
    if "module not found" in msg:
        return "ModuleNotFound"
    if "importerror" in msg:
        return "ImportError"
    if "attributeerror" in msg:
        return "AttributeError"
    if "got multiple values for argument 'options'" in msg:
        return "OptionsConflict"
    if msg.strip() in ["ok", ""]:
        return "OK"
    return "Other"

def run_single_test(args):
    path, test_root, timestamp, project, source_label = args
    step_counter_patch.step_counter["count"] = 0 
    model_name = prompt_type = resolution_key = run_id = module_name = "Unknown"
    model_readable_name = resolution_readable_name = readable_name = "Unknown"
    test_type = "Unknown"
    elapsed = 0
    step_count = 0
    status = "EXCEPTION"
    error_text = ""
    try:
        rel_parts = path.relative_to(test_root).parts
        model_name = rel_parts[0]
        mode = rel_parts[1]
        prompt_type = rel_parts[2]
        if len(rel_parts) == 6:
            resolution_key = rel_parts[3]
            run_id = rel_parts[4]
            module_name = rel_parts[5][:-3]
        elif len(rel_parts) == 5:
            resolution_key = "NO"
            run_id = rel_parts[3]
            module_name = rel_parts[4][:-3]
        test_type = next((tt for (tt, mod) in readable_mapping if mod == module_name), "Unknown")
        readable_name = readable_mapping.get((test_type, module_name), "Unknown")
        model_readable_name = model_readable.get(model_name, "Unknown")
        resolution_readable_name = resolution_readable.get(resolution_key, "Unknown")
        spec = importlib.util.spec_from_file_location("test_module", path)
        test_module = importlib.util.module_from_spec(spec)
        sys.modules["test_module"] = test_module
        spec.loader.exec_module(test_module)
        suite = unittest.defaultTestLoader.loadTestsFromModule(test_module)
        start = time.time()
        result = unittest.TextTestRunner(verbosity=0).run(suite)
        end = time.time()
        elapsed = round(end - start, 2)
        step_count = step_counter_patch.step_counter.get("count", 0)
        error_text = "ok"
        if result.wasSuccessful():
            status = "FALSE_SUCCESS" if elapsed < 0.5 else "SUCCESS"
        elif result.errors:
            status = "ERROR"
            error_text = "\n\n".join(f"{test_id}:\n{trace}" for test_id, trace in result.errors)
        elif result.failures:
            status = "FAIL"
            error_text = "\n\n".join(f"{test_id}:\n{trace}" for test_id, trace in result.failures)
        else:
            status = "UNKNOWN"
            error_text = "unknown result state"
    except Exception as e:
        status = "LOAD_ERROR"
        elapsed = 0
        step_count = 0
        error_text = str(e)
    return [
        timestamp, source_label, project, model_name, model_readable_name, prompt_type,
        resolution_key, resolution_readable_name, run_id, test_type,
        module_name, readable_name, status, elapsed, step_count,
        classify_error(error_text)
    ]
def run_all_tests():
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([
            "Timestamp", "Source", "Project", "Model", "Model Name", "PromptType",
            "Resolution", "Resolution Name", "RunID", "Test Type", "TestModule",
            "ReadableName", "Status", "ExecutionTime(sec)", "Step count", "ErrorType"
        ])
        for project in projects:
            for folder_name, label in sources:
                test_root = base_dir / project / "Processes" / folder_name
                if not test_root.exists():
                    continue
                test_files = [
                    p for p in test_root.rglob("test_*.py")
                    if not any("feedback" in part.lower() for part in p.parts)
                ]
                args_list = [(p, test_root, timestamp, project, label) for p in test_files]
                with ProcessPoolExecutor(max_workers=5) as executor:
                    futures = [executor.submit(run_single_test, args) for args in args_list]
                    all_results = []
                    for future in as_completed(futures):
                        result = future.result()
                        all_results.append(result)
                        with open(output_csv, "a", newline="", encoding="utf-8") as f:
                            writer = csv.writer(f, delimiter=";")
                            writer.writerow(result)


    print(f"FIN - REPORT: {output_csv}")
    return all_results

if __name__ == "__main__":
    all_results = run_all_tests()
    with open(alt_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([
            "Timestamp", "Source", "Project", "Model", "Model Name", "PromptType",
            "Resolution", "Resolution Name", "RunID", "Test Type", "TestModule",
            "ReadableName", "Status", "ExecutionTime(sec)", "Step count", "ErrorType"
        ])
        writer.writerows(all_results)

    print(f"FIN - REPORT_FULL: {alt_csv}")