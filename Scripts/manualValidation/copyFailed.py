import shutil
import csv
from pathlib import Path
csv_path = Path(r"C:\diana\MasterCode\code\Documantation\reports\manualcheck\updatedTestsResults\URLold\shopizerTest.csv")
base_dir = Path(r"C:\diana\MasterCode\code\Projects")
#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
projects = ["shopizer"] 
failed_folder = "failed"
failed_tests = []
with open(csv_path, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if row['Status'].strip().upper() == "SUCCESS":
            continue
        if row['Project'] not in projects:
            continue
        project = row['Project']
        source = row['Source']
        model = row['Model']
        prompt_type = row['PromptType']
        resolution = row['Resolution']
        run_id = row['RunID']
        module = row['TestModule']
        base_path = base_dir / project / "Processes"
        source_path = base_path / source
        test_type = row['Test Type'].strip().lower()
        if test_type == "ui":
            actual_prompt_type = "ui"
        elif test_type == "process":
            actual_prompt_type = "zeroshot"
        else:
            actual_prompt_type = prompt_type  
        subpath_parts = [model, actual_prompt_type, prompt_type]
        if resolution != "NO":
            subpath_parts.append(resolution)
        subpath_parts.append(run_id)
        subpath_parts.append(f"{module}.py")
        rel_path = Path(*subpath_parts)
        src_file = source_path / rel_path
        dest_file = base_path / failed_folder / rel_path
        failed_tests.append((src_file, dest_file))
copied = 0
for src, dst in failed_tests:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    copied += 1
print(f"COPIED: {copied}")
