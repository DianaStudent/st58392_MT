import os
import json
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)
process_name = "checkout"
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


def take_screenshot(driver):
    global screenshot_counter
    filename = os.path.join(screenshots_dir, f"{process_name}_screen{screenshot_counter}.png")
    driver.save_screenshot(filename)
    screenshot_counter += 1

def random_email():
    return f"user_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@test.com"

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

def save_html(name):
    pages_data[name] = driver.page_source
    take_screenshot(driver)

def wait_and_click(selector, by=By.CSS_SELECTOR):
    element = wait.until(EC.element_to_be_clickable((by, selector)))
    driver.execute_script("arguments[0].click();", element)

try:
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
    time.sleep(2)
    
    driver.execute_script("document.body.style.zoom='50%'")
    driver.find_element(By.ID, "termsofservice").click()
    save_html("cart_page")
    wait_and_click("#checkout")
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("checkout_as_guest_or_register")

    driver.execute_script("document.body.style.zoom='50%'")
    wait_and_click("button.checkout-as-guest-button")
    time.sleep(2)
    
    driver.execute_script("document.body.style.zoom='50%'")
    email = random_email()
    driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
    driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
    driver.find_element(By.ID, "BillingNewAddress_Email").send_keys(email)
    driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
    driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
    driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
    driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

    Select(driver.find_element(By.ID, "BillingNewAddress_CountryId")).select_by_value("124")
    time.sleep(1)
    Select(driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")).select_by_value("0")
    save_html("billing_form")
    wait_and_click("button.new-address-next-step-button")
    time.sleep(2)
    driver.execute_script("document.body.style.zoom='50%'")
    wait_and_click("#shippingoption_1")
    save_html("shipping_method_page")
    wait_and_click("button.shipping-method-next-step-button")
    time.sleep(2)
    
    driver.execute_script("document.body.style.zoom='50%'")
    wait_and_click("#paymentmethod_1")
    save_html("payment_method_page")
    wait_and_click("button.payment-method-next-step-button")
    time.sleep(2)
    

    driver.execute_script("document.body.style.zoom='50%'")
    Select(driver.find_element(By.ID, "CreditCardType")).select_by_value("visa")
    driver.find_element(By.ID, "CardholderName").send_keys("Test User")
    driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
    Select(driver.find_element(By.ID, "ExpireMonth")).select_by_value("4")
    Select(driver.find_element(By.ID, "ExpireYear")).select_by_value("2027")
    driver.find_element(By.ID, "CardCode").send_keys("123")
    save_html("payment_info_page")
    wait_and_click("button.payment-info-next-step-button")
    time.sleep(2)
    save_html("confirm_order_page")

    driver.execute_script("document.body.style.zoom='50%'")
    wait_and_click("button.confirm-order-next-step-button")
    time.sleep(3)
    save_html("order_completed")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)

    print(f"FIN: {output_file}")

finally:
    driver.quit()
