import csv
import subprocess
from pathlib import Path

csv_path = Path(r"C:\diana\MasterCode\code\Documantation\reports\manualcheck\updatedTestsResults\URL\medusaTestGeminiFix.csv")
#csv_path = Path(r"C:\diana\MasterCode\code\Documantation\reports\manualcheck\updatedTestsResults\URL\CezerinTestDriver.csv")
base_dir = Path(r"C:\diana\MasterCode\code\projects")
#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
project = "medusa"
sources = ["tests", "testsURLchange", "testsDriverChange", "failed"]
batch_size = 25
main_script = "runALL.py"

def load_completed_tests():
    completed = set()
    if not csv_path.exists():
        return completed
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if row["Status"] in ["SUCCESS", "FALSE_SUCCESS"]:
                key = (
                    row["Source"],
                    row["Model"],
                    row["PromptType"],
                    row["Resolution"],
                    row["RunID"],
                    row["TestModule"]
                )
                completed.add(key)
    return completed

def find_all_tests():
    tests = []
    for source in sources:
        root = base_dir / project / "Processes" / source
        if not root.exists():
            continue
        for path in root.rglob("test_*.py"):
            if any("feedback" in part.lower() for part in path.parts):
                continue
            rel = path.relative_to(root)
            parts = rel.parts
            if len(parts) == 6:
                model, _, prompt_type, resolution, run_id, file = parts
            elif len(parts) == 5:
                model, _, prompt_type, run_id, file = parts
                resolution = "NO"
            else:
                continue
            module = file.stem
            key = (source, model, prompt_type, resolution, run_id, module)
            tests.append((key, path))
    return tests

completed = load_completed_tests()
all_tests = find_all_tests()
pending_tests = [path for key, path in all_tests if key not in completed]
batch = pending_tests[:batch_size]
temp_file = "batch_tests.txt"
Path(temp_file).write_text("\n".join(str(p) for p in batch), encoding="utf-8")
env = dict(**subprocess.os.environ)
env["batch_file"] = temp_file
subprocess.run(["python", main_script], env=env)
Path(temp_file).unlink()

print(f"FIN")