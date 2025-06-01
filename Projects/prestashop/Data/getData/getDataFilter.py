import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


process_name = "filter"
base_dir = r"C:\diana\MasterCode\code\Projects\prestashop\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

BASE_URL = "http://localhost:8080/en/"

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 20)
pages_data = {}
screenshot_counter = 1

def take_screenshot():
    global screenshot_counter
    time.sleep(1)
    filename = os.path.join(screenshots_dir, f"{process_name}_screen{screenshot_counter}.png")
    driver.save_screenshot(filename)
    screenshot_counter += 1

def save_html(name):
    pages_data[name] = driver.page_source
    take_screenshot()

def apply_filter_by_label(section_name, label_text):
    wait.until(EC.presence_of_element_located((By.ID, "search_filters_wrapper")))
    xpath = (
        f"//section[@class='facet clearfix' and @data-name='{section_name}']"
        f"//label[contains(., '{label_text}')]//input[@type='checkbox']"
    )
    checkbox = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", checkbox)
    driver.execute_script("document.body.style.zoom='50%'")
    save_html(f"filter_{section_name.lower()}_{label_text.lower().replace(' ', '_')}")


try:
    driver.get(BASE_URL)
    time.sleep(2)
    save_html("home_page")

    art_link = driver.find_element(By.CSS_SELECTOR, '#top-menu a[href*="/9-art"]')
    art_link.click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("art_category_page")
    apply_filter_by_label("Composition", "Matt paper")
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".js-product")
    clear_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-search-filters-clear-all")))
    driver.execute_script("arguments[0].click();", clear_button)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(3)
    save_html("after_clear_filter")
    products = driver.find_elements(By.CSS_SELECTOR, ".js-product")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
