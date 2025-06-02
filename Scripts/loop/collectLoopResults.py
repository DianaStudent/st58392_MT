import os
import csv
import re
projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
#projects = ["medusa"] 
# model = "gpt-4o" 
model = "gemini"
results_dir = r"C:\Diana\MasterCode\code\Documantation"
csv_output = os.path.join(results_dir, f"feedback_report_all_gemini.csv")
def extract_cycle_number(filename):
    match = re.search(r'_v(\d+)\.py$', filename)
    return int(match.group(1)) if match else -1
file_exists = os.path.isfile(csv_output)
with open(csv_output, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["project", "model", "run", "process", "status", "cycle"])
    if not file_exists:
        writer.writeheader()
    for project in projects:
        base_path = rf"C:\Diana\MasterCode\code\Projects\{project}\Processes\tests\{model}\feedback"
        for run_folder in sorted(os.listdir(base_path)):
            run_path = os.path.join(base_path, run_folder)
            loops_path = os.path.join(run_path, "loops")
            success_path = os.path.join(run_path, "success")
            results = {}
            if os.path.isdir(loops_path):
                for filename in os.listdir(loops_path):
                    if not filename.endswith(".py"):
                        continue
                    name_part = filename.replace(".py", "")
                    process_name = name_part.rsplit("_v", 1)[0]
                    version = extract_cycle_number(filename)
                    if process_name not in results:
                        results[process_name] = {
                            "project": project,
                            "model": model,
                            "run": run_folder,
                            "process": process_name,
                            "status": "FAIL",
                            "cycle": version
                        }
                    else:
                        results[process_name]["cycle"] = max(results[process_name]["cycle"], version)
            if os.path.isdir(success_path):
                for filename in os.listdir(success_path):
                    if not filename.endswith(".py"):
                        continue
                    name_part = filename.replace(".py", "")
                    process_name = name_part.rsplit("_v", 1)[0]
                    version = extract_cycle_number(filename)
                    results[process_name] = {
                        "project": project,
                        "model": model,
                        "run": run_folder,
                        "process": process_name,
                        "status": "SUCCESS",
                        "cycle": version
                    }
            for item in results.values():
                writer.writerow(item)

print(f"CSV: {csv_output}")
