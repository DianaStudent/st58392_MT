import os
import json
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)
process_name = "register"

base_dir = r"C:\Diana\Master\MasterCode\code\Projects\nopCommerce\Processes"
output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")
os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

driver.maximize_window()
screenshot_counter = 1
unique_email = f"test_{uuid.uuid4().hex[:6]}@user.com"

BASE_URL = "http://max/"
form_data = {
    "Gender": "F",
    "FirstName": "Test",
    "LastName": "User",
    "Email": unique_email,
    "Company": "TestCorp",
    "Password": "test11",
    "ConfirmPassword": "test11"
}

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
    save_html("home_before_register")

    register_link = driver.find_element(By.CSS_SELECTOR, "a.ico-register")
    register_link.click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("register_page")

    if form_data["Gender"] == "F":
        driver.find_element(By.ID, "gender-female").click()
    else:
        driver.find_element(By.ID, "gender-male").click()

    driver.find_element(By.ID, "FirstName").send_keys(form_data["FirstName"])
    driver.find_element(By.ID, "LastName").send_keys(form_data["LastName"])
    driver.find_element(By.ID, "Email").send_keys(form_data["Email"])
    driver.find_element(By.ID, "Company").send_keys(form_data["Company"])
    driver.find_element(By.ID, "Password").send_keys(form_data["Password"])
    driver.find_element(By.ID, "ConfirmPassword").send_keys(form_data["ConfirmPassword"])

    driver.find_element(By.ID, "register-button").click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(3)
    save_html("register_result")

    try:
        result_text = driver.find_element(By.CSS_SELECTOR, ".result").text
    except Exception:
        print("ERROR")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
