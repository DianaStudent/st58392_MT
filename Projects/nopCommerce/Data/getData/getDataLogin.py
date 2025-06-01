import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)

process_name = "login"
base_dir = r"C:\Diana\Master\MasterCode\code\Projects\nopCommerce\Processes"
output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

driver.maximize_window()
screenshot_counter = 1

BASE_URL = "http://max/"
LOGIN = "admin@admin.com"
PASSWORD = "admin"

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
    save_html("home_before_login")

    login_link = driver.find_element(By.CSS_SELECTOR, 'a.ico-login')
    login_link.click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("login_page")
    driver.find_element(By.ID, "Email").send_keys(LOGIN)
    driver.find_element(By.ID, "Password").send_keys(PASSWORD)
    time.sleep(3)
    save_html("after_login")
    driver.find_element(By.CSS_SELECTOR, "button.login-button").click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(3)
    save_html("after_login")

    try:
        account_link = driver.find_element(By.CSS_SELECTOR, "a.ico-account")
    except Exception:
        print("ERROR")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
