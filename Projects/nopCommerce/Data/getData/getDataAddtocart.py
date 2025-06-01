import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)

process_name = "addtocart"
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

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 15)
pages_data = {}

def take_screenshot(driver):
    global screenshot_counter
    filename = os.path.join(screenshots_dir, f"{process_name}_screen{screenshot_counter}.png")
    driver.save_screenshot(filename)
    screenshot_counter += 1

def save_html(name):
    pages_data[name] = driver.page_source
    take_screenshot(driver)

def wait_and_click(selector, by=By.CSS_SELECTOR):
    element = wait.until(EC.element_to_be_clickable((by, selector)))
    driver.execute_script("arguments[0].click();", element)

try:
    os.makedirs(output_dir, exist_ok=True)
    driver.get(BASE_URL)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("home")

    driver.find_element(By.LINK_TEXT, "Search").click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(1)
    

    driver.find_element(By.ID, "q").send_keys(SEARCH_TERM)
    save_html("search_page")
    driver.find_element(By.CSS_SELECTOR, "button.search-button").click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("search_results")

    wait_and_click("button.product-box-add-to-cart-button")
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("after_add_to_cart")

    wait_and_click(".bar-notification.success a")
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)    
    save_html("cart_page")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)

    print(f"FIN: {output_file}")

finally:
    driver.quit()
