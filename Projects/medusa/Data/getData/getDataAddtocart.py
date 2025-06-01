import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

process_name = "addtocart"
base_dir = r"C:\Diana\MasterCode\code\Projects\medusa\Processes"

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
    driver.get("http://localhost:8000/dk")
    driver.execute_script("document.body.style.zoom='100%'")
    time.sleep(2)
    save_html("home_page")

    menu_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='nav-menu-button']")
    menu_button.click()
    time.sleep(1)
    save_html("menu_opened")

    store_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='store-link']")
    store_link.click()
    time.sleep(2)
    save_html("store_page")

    product_image = driver.find_element(By.CSS_SELECTOR, "img[alt='Thumbnail']")
    product_image.click()
    time.sleep(2)
    save_html("product_page")

    size_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='option-button']")
    size_button.click()
    time.sleep(1)
    save_html("size_selected")

    add_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='add-product-button']")
    add_button.click()
    time.sleep(2)
    save_html("product_added")

    cart_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='nav-cart-link']")
    cart_link.click()
    time.sleep(2)
    save_html("cart_page")

    cart_row = driver.find_element(By.CSS_SELECTOR, "[data-testid='product-row']")
    assert cart_row is not None

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
