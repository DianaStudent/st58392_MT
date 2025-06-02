import shutil
import re
from pathlib import Path

projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
base_dir = r"C:\Diana\MasterCode\code\projects"
source_subfolder = Path("Processes") / "tests"
target_subfolder = Path("Processes") / "testsURLchange"

project_base_urls = {
    "Cezerin": {
        "addtocart": "http://localhost:3000/",
        "checkout": "http://localhost:3000/",
        "filter": "http://localhost:3000/category-a",
    },
    "shopizer": "http://localhost/",
    "prestashop": "http://localhost:8080/en/",
    "nopCommerce": "http://max/",
    "medusa": "http://localhost:8000/dk",
}

ui_url_mappings = {
    "Cezerin": {
        "home": "http://localhost:3000",
        "category_a": "http://localhost:3000/category-a",
        "category_a_1": "http://localhost:3000/category-a-1",
    },
    "nopCommerce": {
        "home": "http://max/",
        "login_page": "http://max/login?returnUrl=%2F",
        "register_page": "http://max/register?returnUrl=%2F",
        "search_page": "http://max/search",
    },
    "prestashop": {
        "home": "http://localhost:8080/en/",
        "clothes": "http://localhost:8080/en/3-clothes",
        "accessories": "http://localhost:8080/en/6-accessories",
        "art": "http://localhost:8080/en/9-art",
        "login": "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art",
        "register": "http://localhost:8080/en/registration",
    },
    "shopizer": {
        "home": "http://localhost/",
        "tables": "http://localhost/category/tables",
        "chairs": "http://localhost/category/chairs",
        "login": "http://localhost/login",
        "register": "http://localhost/register",
    }
}

def is_correct_url(url, project, filename):
    if project == "Cezerin":
        fname = filename.lower()
        if "addtocart" in fname or "checkout" in fname:
            return url.startswith(project_base_urls["Cezerin"]["addtocart"])
        elif "filter" in fname:
            return url.startswith(project_base_urls["Cezerin"]["filter"])
        return True
    else:
        expected = project_base_urls.get(project)
        return url.startswith(expected)

def get_correct_url(project, filename, filepath):
    if "ui" in str(filepath).lower().replace("\\", "/"):
        fname = filename.lower()
        mapping = ui_url_mappings.get(project, {})
        for key, url in mapping.items():
            if key in fname:
                return url
        return None
    if project == "Cezerin":
        fname = filename.lower()
        if "addtocart" in fname or "checkout" in fname:
            return project_base_urls["Cezerin"]["addtocart"]
        elif "filter" in fname:
            return project_base_urls["Cezerin"]["filter"]
        return None
    return project_base_urls.get(project)

def replace_urls_in_file(filepath, project, filename):
    content = filepath.read_text(encoding="utf-8")
    url_patterns = re.findall(r'((?:self\.)?driver\.get\(\s*)([\'"])(.*?)([\'"]\s*\))', content)
    assignment_patterns = re.findall(r'((?:self\.)?(?:url|URL)\s*=\s*)([\'"])(.*?)([\'"])', content)
    replaced = False
    for prefix, quote, url, suffix in url_patterns + assignment_patterns:
        if not is_correct_url(url, project, filename):
            correct_url = get_correct_url(project, filename, filepath)
            if correct_url:
                pattern = re.escape(prefix) + re.escape(quote) + re.escape(url) + re.escape(quote) + re.escape(suffix)
                replacement = f"{prefix}{quote}{correct_url}{quote}{suffix}"
                content = re.sub(pattern, replacement, content)
                replaced = True
    if replaced:
        filepath.write_text(content, encoding="utf-8")
        
for project in projects:
    src_dir = base_dir / project / source_subfolder
    dst_dir = base_dir / project / target_subfolder
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir)
    for filepath in dst_dir.rglob("*.py"):
        replace_urls_in_file(filepath, project, filepath.name)

print("FIN")
