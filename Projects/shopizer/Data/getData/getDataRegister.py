import os
import json
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

process_name = "register"
base_dir = r"C:\diana\MasterCode\code\Projects\shopizer\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)
BASE_URL = "http://localhost/"
unique_email = f"test_{uuid.uuid4().hex[:6]}@user.com"
form_data = {
    "Email": unique_email,
    "Password": "test**11",
    "RepeatPassword": "test**11",
    "FirstName": "Test",
    "LastName": "User"
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
    driver.execute_script("document.body.style.zoom='75%'")
    time.sleep(2)
    save_html("home_before_register")
    driver.find_element(By.CSS_SELECTOR, "button.account-setting-active").click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
    time.sleep(2)
    #save_html("register_page")
    driver.find_element(By.NAME, "email").send_keys(form_data["Email"])
    driver.find_element(By.NAME, "password").send_keys(form_data["Password"])
    driver.find_element(By.NAME, "repeatPassword").send_keys(form_data["RepeatPassword"])
    driver.find_element(By.NAME, "firstName").send_keys(form_data["FirstName"])
    driver.find_element(By.NAME, "lastName").send_keys(form_data["LastName"])
    selects = driver.find_elements(By.TAG_NAME, "select")
    country_select = None
    for s in selects:
        try:
            first_option = s.find_element(By.TAG_NAME, "option").text.strip().lower()
            if "country" in first_option:
                country_select = s
                break
        except:
            continue

    driver.execute_script("""arguments[0].selectedIndex = 1;arguments[0].dispatchEvent(new Event('change', { bubbles: true }));""", country_select)
    time.sleep(3)

    def find_state_select(drv):
        for sel in drv.find_elements(By.TAG_NAME, "select"):
            try:
                first_option = sel.find_element(By.TAG_NAME, "option").text.strip().lower()
                if "state" in first_option:
                    return sel
            except:
                continue
        return False

    region_select = WebDriverWait(driver, 10).until(find_state_select)

    driver.execute_script("""arguments[0].selectedIndex = 1;arguments[0].dispatchEvent(new Event('change', { bubbles: true }));""", region_select)
    time.sleep(1)
    driver.find_element(By.TAG_NAME, "body").click()
    driver.execute_script("document.body.style.zoom='65%'")
    save_html("filled_register_form")
    register_button = driver.find_element(By.XPATH, "//button[span[text()='Register']]")
    driver.execute_script("arguments[0].scrollIntoView(true);", register_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(2)
    save_html("register_result")
    current_url = driver.current_url
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN:: {output_file}")

finally:
    driver.quit()
