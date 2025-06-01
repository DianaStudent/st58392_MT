import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

process_name = "addtocart"
base_dir = r"C:\diana\MasterCode\code\Projects\shopizer\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

BASE_URL = "http://localhost/"

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
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
    driver.execute_script("document.body.style.zoom='75%'")
    time.sleep(2)
    save_html("home_page")

    products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")[:2]
    for i, product in enumerate(products):
        hover_target = product.find_element(By.CLASS_NAME, "product-img")
        actions.move_to_element(hover_target).perform()
        time.sleep(1)
        add_btn = product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
        driver.execute_script("arguments[0].click();", add_btn)
        time.sleep(2)
    save_html("after_add_to_cart")

    cart_button = driver.find_element(By.CSS_SELECTOR, "button.icon-cart")
    cart_button.click()
    time.sleep(2)
    save_html("cart_popup_opened")

    view_cart_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping-cart-btn a[href='/cart']"))
    )
    driver.execute_script("arguments[0].click();", view_cart_btn)
    time.sleep(2)
    save_html("cart_page")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
