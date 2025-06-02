from pathlib import Path
import csv
import shutil

#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
project = "Cezerin"
base_dir = Path(r"C:\Diana\Master\MasterCode\code\Projects")
csv_path = Path(r"C:\Diana\Master\MasterCode\code\Documantation\Visualizations\origForMutationcollect\tests_report_ALL.csv")
success_dir = base_dir / project / "Processes" / "tests" / "Success"
success_dir.mkdir(parents=True, exist_ok=True)

with csv_path.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if not row or row.get("Status") is None:
            continue
        if row["Status"].strip().upper() != "SUCCESS":
            continue
        if row["Project"].strip() != project:
            continue
        model = row["Model"]
        prompt_type = row["PromptType"]
        resolution = row["Resolution"]
        run_id = row["RunID"]
        test_module = row["TestModule"]
        test_path = base_dir / project / "Processes" / "tests" / model / "zeroshot" / prompt_type / resolution / run_id / f"{test_module}.py"
        new_name = f"{model}__{prompt_type}__{resolution}__{run_id}__{test_module}.py"
        dest_path = success_dir / new_name
        shutil.copy2(test_path, dest_path)
        print(f"COPIED: {dest_path}")

