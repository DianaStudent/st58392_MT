import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

process_name = "addtocart"
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
    driver.get("http://localhost:3000/")
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("home_page")
    category_a = driver.find_element(By.XPATH, "//a[@href='/category-a' and contains(text(),'Category A')]")
    category_a.click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("category_a_page")
    product_a = driver.find_element(By.XPATH, "//a[@href='/category-a/product-a']")
    product_a.click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("product_page")
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "button-addtocart").find_element(By.TAG_NAME, "button")
    add_to_cart_button.click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    popup = driver.find_element(By.CLASS_NAME, "mini-cart")
    save_html("popup")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
