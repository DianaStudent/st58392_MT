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

process_name = "addtocart"
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

wait = WebDriverWait(driver, 15)
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

try:
    driver.get(BASE_URL)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("home_before_login")

    art_link = driver.find_element(By.CSS_SELECTOR, '#top-menu a[href*="/9-art"]')
    driver.execute_script("arguments[0].click();", art_link)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("art_category_page")

    product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-product .product-title a")))
    driver.execute_script("arguments[0].click();", product_link)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("product_detail_page")

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart")))
    driver.execute_script("arguments[0].click();", add_to_cart_button)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(3)
    save_html("after_add_to_cart")

    try:
        modal_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content .modal-title")))
    except Exception as e:
        print("ERROR: ", str(e))

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
