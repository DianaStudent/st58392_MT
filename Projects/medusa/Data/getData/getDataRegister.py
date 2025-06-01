import os
import json
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

process_name = "register"
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

unique_email = f"user_{uuid.uuid4().hex[:6]}@test.com"
form_data = {
    "first_name": "user",
    "last_name": "test",
    "email": unique_email,
    "phone": "12345678",
    "password": "testuser"
}

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

    account_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='nav-account-link']")
    account_link.click()
    time.sleep(2)
    save_html("account_page")

    join_us_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
    join_us_button.click()
    time.sleep(2)
    save_html("register_form")

    driver.find_element(By.NAME, "first_name").send_keys(form_data["first_name"])
    driver.find_element(By.NAME, "last_name").send_keys(form_data["last_name"])
    driver.find_element(By.NAME, "email").send_keys(form_data["email"])
    driver.find_element(By.NAME, "phone").send_keys(form_data["phone"])
    driver.find_element(By.NAME, "password").send_keys(form_data["password"])
    save_html("form_filled")

    driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button'][type='submit']").click()
    time.sleep(3)
    save_html("registration_result")

    try:
        welcome_text = driver.find_element(By.CSS_SELECTOR, "[data-testid='welcome-message']").text
        email_shown = driver.find_element(By.CSS_SELECTOR, "[data-testid='customer-email']").text
    except Exception:
        print("ERROR")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
