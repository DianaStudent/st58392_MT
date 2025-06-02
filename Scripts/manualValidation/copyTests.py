import shutil
from pathlib import Path
import csv
csv_path = Path(r"C:\Diana\Master\MasterCode\code\Visualizations\ManualValidation\manualSelectURLallcsv.csv")
base_dir = Path(r"C:\Diana\Master\MasterCode\code\Projects")
dest_folder = Path(r"C:\Diana\Master\MasterCode\code\Documantation\reports\manualcheck\testsURLall_names")
copied = 0
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if row['UpdateStatus'].strip().upper() != 'MB':
            continue
        project = row['Project']
        model = row['Model']
        prompt_type = row['PromptType']
        resolution = str(row['Resolution'])
        run_id = str(row['RunID'])
        module = row['TestModule']
        error_type = row['ErrorType']
        base_path = base_dir / project / "Processes"
        path_parts = [base_path, "tests", model, "zeroshot", prompt_type]
        if resolution != 'NO':
            path_parts.append(resolution)
        path_parts.append(run_id)
        src_file = Path(*path_parts) / f"{module}.py"
        if not src_file.is_file():
            continue
        name_parts = [error_type, project, model, prompt_type]
        if resolution != 'NO':
            name_parts.append(resolution)
        name_parts.extend([run_id, module])
        dest_file = dest_folder / f"{'_'.join(name_parts)}.py"
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dest_file)
        copied += 1

print(f"COPIED: {copied}")