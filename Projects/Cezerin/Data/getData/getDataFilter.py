import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

process_name = "filter"
base_dir = r"C:\Diana\Master\MasterCode\code\Projects\Cezerin\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
pages_data = {}
screenshot_counter = 1

def take_screenshot():
    global screenshot_counter
    filename = os.path.join(screenshots_dir, f"{process_name}_screen{screenshot_counter}.png")
    driver.save_screenshot(filename)
    screenshot_counter += 1

def save_html(name):
    pages_data[name] = driver.page_source
    take_screenshot()

try:
    driver.get("http://localhost:3000/category-a")
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("category_a_initial")
    brand_a_checkbox = driver.find_element(By.XPATH, "//label[contains(.,'Brand A')]/input[@type='checkbox']")
    brand_a_checkbox.click()
    time.sleep(2)
    save_html("filter_brand_a_selected")
    brand_a_checkbox.click()
    time.sleep(2)
    save_html("filter_brand_a_unselected")

    driver.get("http://localhost:3000/category-a?price_from=967&price_to=1250")
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("filter_price_range")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
