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

options = Options()
driver = webdriver.Chrome(options=options)


process_name = "login"
base_dir = r"C:\diana\MasterCode\code\Projects\prestashop\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

BASE_URL = "http://localhost:8080/en/"
login_data = {
    "Email": "test@user.com",
    "Password": "test@user1"
}


options = Options()
# options.add_argument("--headless") 
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)
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
    #driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("home_before_login")

    sign_in_button = driver.find_element(By.CSS_SELECTOR, '#_desktop_user_info a[href*="login"]')
    driver.execute_script("arguments[0].click();", sign_in_button)
    #driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    #save_html("login_page")
    email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
    password_input = driver.find_element(By.ID, "field-password")
    email_input.send_keys(login_data["Email"])
    password_input.send_keys(login_data["Password"])
   # driver.execute_script("document.body.style.zoom='50%'")
    save_html("filled_login_form")

    submit_btn = driver.find_element(By.ID, "submit-login")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", submit_btn)
    #driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(3)
    save_html("login_result")
    user_info_block = driver.find_element(By.ID, "_desktop_user_info").get_attribute("innerHTML")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN:: {output_file}")

finally:
    driver.quit()
