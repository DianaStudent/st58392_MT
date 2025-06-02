import re
import shutil
from pathlib import Path

projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
base_dir = Path(r"C:\Diana\MasterCode\code\projects")
from_import_line = "from selenium.webdriver.chrome.service import Service as ChromeService"

def fix_driver_instantiation(file_path):
    with file_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    updated_lines = []
    changed = False
    for line in lines:
        if "webdriver.Chrome(ChromeDriverManager().install())" in line:
            indent = re.match(r"^(\s*)", line).group(1)
            new_line = f"{indent}self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))\n"
            updated_lines.append(new_line)
            changed = True
        else:
            updated_lines.append(line)
    if changed and all(from_import_line not in l for l in updated_lines):
        insert_index = 0
        for i, l in enumerate(updated_lines):
            if l.strip().startswith(("import", "from")):
                insert_index = i + 1
        updated_lines.insert(insert_index, from_import_line + "\n")
    if changed:
        with file_path.open("w", encoding="utf-8") as f:
            f.writelines(updated_lines)
        print(f"FIXED: {file_path}")

for project in projects:
    src = base_dir / project / "Processes" / "testsURLchange"
    dst = base_dir / project / "Processes" / "testsDriverChange"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    for file in dst.rglob("*.py"):
        fix_driver_instantiation(file)

print("FIN")
