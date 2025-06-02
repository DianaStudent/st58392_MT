import csv
import shutil
from pathlib import Path
from collections import defaultdict

project_counts = defaultdict(int)

csv_path = Path(r"C:\diana\MasterCode\code\Visualizations\Results\all_fulldump_fin.csv")
base_dir = Path(r"C:\Diana\MasterCode\code\Projects")
#projects = {"Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"}
projects = {"shopizer", "prestashop", "nopCommerce", "medusa"}
source = {"testsDriverChange"}
addition_source = "failed"

def get_test_type_folder(test_type):
    return "zeroshot" if test_type == "process" else "ui"
successful_keys = set()

with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if row["Status"] not in ["SUCCESS"]:
            continue
        project = row["Project"]
        source = row["Source"]
        if project not in projects or source not in source:
            continue
        key = (
            project, row["Model"], row["PromptType"], row["Resolution"],
            row["RunID"], row["Test Type"], row["TestModule"]
        )
        successful_keys.add(key)
        model = row["Model"]
        prompt_type = row["PromptType"]
        resolution = row["Resolution"]
        run_id = row["RunID"]
        test_type = row["Test Type"]
        if test_type == "ui":
            continue
        module = row["TestModule"]
        test_folder = get_test_type_folder(test_type)
        parts = [base_dir, project, "Processes", source, model, test_folder, prompt_type]
        if resolution != "NO":
            parts.append(resolution)
        parts.append(run_id)
        test_path = Path(*parts) / (module + ".py")
        dest_dir = base_dir / project / "Processes" / "collectedSuccess"
        dest_dir.mkdir(parents=True, exist_ok=True)
        name_parts = [model, prompt_type]
        if resolution != "NO":
            name_parts.append(resolution)
        name_parts.extend([run_id, test_folder, module])
        dest_name = "__".join(name_parts) + ".py"
        dest_path = dest_dir / dest_name
        shutil.copy2(test_path, dest_path)
        project_counts[project] += 1

with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if row["Status"] not in ["SUCCESS"]:
            continue
        project = row["Project"]
        source = row["Source"]
        if project not in projects or source != addition_source:
            continue
        key = (
            project, row["Model"], row["PromptType"], row["Resolution"],
            row["RunID"], row["Test Type"], row["TestModule"]
        )
        if key in successful_keys:
            continue 
        model = row["Model"]
        prompt_type = row["PromptType"]
        resolution = row["Resolution"]
        run_id = row["RunID"]
        test_type = row["Test Type"]
        if test_type == "ui":
            continue
        module = row["TestModule"]
        test_folder = get_test_type_folder(test_type)
        parts = [base_dir, project, "Processes", source, model, test_folder, prompt_type]
        if resolution != "NO":
            parts.append(resolution)
        parts.append(run_id)
        test_path = Path(*parts) / (module + ".py")
        dest_dir = base_dir / project / "Processes" / "collectedSuccess"
        dest_dir.mkdir(parents=True, exist_ok=True)
        name_parts = [model, prompt_type]
        if resolution != "NO":
            name_parts.append(resolution)
        name_parts.extend([run_id, test_folder, module])
        dest_name = "__".join(name_parts) + ".py"
        dest_path = dest_dir / dest_name
        project_counts[project] += 1
        shutil.copy2(test_path, dest_path)
for project, count in sorted(project_counts.items()):
    print(f" FIN {project}: {count}")