from pathlib import Path
#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
projects = ["shopizer"]
base_dir = Path(r"C:\diana\MasterCode\code\Projects")
clickable_patterns = [
    'button', 'href', 'nav-', '-input', 'input#', 'input.', 'input[', 'select[', 'select#',
    'section[', 'cart-icon', 'a.', 'link', 'icon-cart', 'add-to-cart', 'checkbox', 'option',
    'send_keys', '.click', '_input', '_field'
]
non_clickable_patterns = ['message', 'form', 'thank', 'successfully']
import_line = "from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element"

for project in projects:
    failed_dir = base_dir / project / "Processes" / "failed"
    if not failed_dir.exists():
        continue
    for file_path in failed_dir.rglob("*.py"):
        lines = file_path.read_text(encoding="utf-8").splitlines(keepends=True)
        updated_lines = []
        changed = False
        for line in lines:
            lowered = line.lower()
            if "presence_of_element_located" in line and any(p in lowered for p in clickable_patterns):
                line = line.replace("presence_of_element_located", "element_to_be_clickable")
                changed = True
            elif "element_to_be_clickable" in line and any(p in lowered for p in non_clickable_patterns):
                line = line.replace("element_to_be_clickable", "presence_of_element_located")
                changed = True
            updated_lines.append(line)
        if not any(import_line in l for l in updated_lines):
            updated_lines.insert(0, import_line + "\n")
            changed = True
        if changed:
            file_path.write_text("".join(updated_lines), encoding="utf-8")
            print(f"FIXED: {file_path}")
print("FIN")
