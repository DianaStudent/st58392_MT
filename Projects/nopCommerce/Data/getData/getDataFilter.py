import os
import json
import time
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)

process_name = "filter"
base_dir = r"C:\Diana\Master\MasterCode\code\Projects\nopCommerce\Processes"
output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

driver.maximize_window()
screenshot_counter = 1

BASE_URL = "http://max/"
SEARCH_TERM = "book"
BASE_QUERY = {
    "viewmode": "grid",
    "orderby": 0,
    "pagesize": 6,
    "q": SEARCH_TERM,
    "advs": "false"
}
FILTERS = [
    {"label": "0_15", "price": "0-25"},
    {"label": "15_25", "price": "15-50"}
]

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

pages_data = {}

def take_screenshot(driver):
    global screenshot_counter
    filename = os.path.join(screenshots_dir, f"{process_name}_screen{screenshot_counter}.png")
    driver.save_screenshot(filename)
    screenshot_counter += 1

def save_html(name):
    pages_data[name] = driver.page_source
    take_screenshot(driver)


try:
    os.makedirs(output_dir, exist_ok=True)
    driver.get(BASE_URL)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("base")

    search_link = driver.find_element(By.LINK_TEXT, "Search")
    search_link.click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("search_page_before")

    search_input = driver.find_element(By.ID, "q")
    search_input.send_keys(SEARCH_TERM)

    driver.find_element(By.CSS_SELECTOR, "button.search-button").click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("search_results_book")

    for filt in FILTERS:
        label = filt["label"]
        full_query = BASE_QUERY.copy()
        full_query["price"] = filt["price"]
        url = f"{BASE_URL}search?{urlencode(full_query)}"
        driver.get(url)
        driver.execute_script("document.body.style.zoom='50%'")
        time.sleep(2)
        save_html(f"search_filter_{label}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)

    print(f"FIN: {output_file}")

finally:
    driver.quit()
