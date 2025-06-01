import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


process_name = "UI"
base_dir = r"C:\diana\MasterCode\code\Projects\prestashop\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
screenshots_base_dir = os.path.join(base_dir, "data", "screenshots", "source", process_name)
output_file = os.path.join(output_dir, f"{process_name}_html.json")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_base_dir, exist_ok=True)

pages = {
    "home": "http://localhost:8080/en/",
    "clothes": "http://localhost:8080/en/3-clothes",
    "accessories": "http://localhost:8080/en/6-accessories",
    "art": "http://localhost:8080/en/9-art",
    "login": "http://localhost:8080/en/login",
    "register": "http://localhost:8080/en/registration"
}

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

pages_data = {}

def take_screenshot(page_name):
    """Создает папку и сохраняет скриншот"""
    page_screenshot_dir = os.path.join(screenshots_base_dir, page_name)
    os.makedirs(page_screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(page_screenshot_dir, f"{page_name}.png")
    driver.save_screenshot(screenshot_path)

def save_html(page_name):
    pages_data[page_name] = driver.page_source

    take_screenshot(page_name)

try:
    for name, url in pages.items():
        driver.get(url)
        driver.execute_script("document.body.style.zoom='50%'")
        time.sleep(3)
        save_html(name)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
