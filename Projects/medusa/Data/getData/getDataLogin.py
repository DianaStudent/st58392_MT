import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

process_name = "login"
base_dir = r"C:\Diana\MasterCode\code\Projects\Medusa\Processes"
output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

LOGIN = "user@test.com"
PASSWORD = "testuser"

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
    save_html("home_before_login")

    account_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='nav-account-link']")
    account_link.click()
    time.sleep(2)
    save_html("login_page")

    driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']").send_keys(LOGIN)
    driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']").send_keys(PASSWORD)
    save_html("credentials_entered")

    driver.find_element(By.CSS_SELECTOR, "[data-testid='sign-in-button']").click()
    time.sleep(3)
    save_html("after_login")
    try:
        welcome = driver.find_element(By.CSS_SELECTOR, "[data-testid='welcome-message']").text
        email = driver.find_element(By.CSS_SELECTOR, "[data-testid='customer-email']").text
    except Exception:
        print("ERROR")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
