import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


process_name = "addtocart"
base_dir = os.path.join("..", "separateTests", "Processes", "process_data")
output_file = os.path.join(base_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "screenshots", f"{process_name}_screen")
os.makedirs(screenshots_dir, exist_ok=True)

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1500

BASE_URL = "http://localhost:8080/en/"
login_data = {
    "Email": "test@user88.com",
    "Password": "test@user88"
}

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

wait = WebDriverWait(driver, 10)
pages_data = {}
screenshot_counter = 1

def save_html(name):
    pages_data[name] = driver.page_source

def take_screenshot():
    global screenshot_counter
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(WINDOW_WIDTH, scroll_height)
    time.sleep(1)
    path = os.path.join(screenshots_dir, f"{process_name}_screen{screenshot_counter}.png")
    driver.save_screenshot(path)
    screenshot_counter += 1



try:
    driver.get(BASE_URL)
    time.sleep(2)
    save_html("home_before_login")
    take_screenshot()

    sign_in_button = driver.find_element(By.CSS_SELECTOR, '#_desktop_user_info a[href*="login"]')
    driver.execute_script("arguments[0].click();", sign_in_button)
    time.sleep(2)
    save_html("login_page")
    take_screenshot()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
    password_input = driver.find_element(By.ID, "field-password")
    email_input.send_keys(login_data["Email"])
    password_input.send_keys(login_data["Password"])
    save_html("filled_login_form")
    take_screenshot()

    submit_btn = driver.find_element(By.ID, "submit-login")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    driver.execute_script("arguments[0].click();", submit_btn)
    time.sleep(3)
    save_html("login_result")
    take_screenshot()

    art_link = driver.find_element(By.CSS_SELECTOR, '#top-menu a[href*="/9-art"]')
    driver.execute_script("arguments[0].click();", art_link)
    time.sleep(2)
    save_html("art_category_page")
    take_screenshot()

    product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-product .product-title a")))
    driver.execute_script("arguments[0].click();", product_link)
    time.sleep(2)
    save_html("product_detail_page")
    take_screenshot()

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart")))
    driver.execute_script("arguments[0].click();", add_to_cart_button)
    time.sleep(1)
    save_html("after_add_to_cart")
    take_screenshot()
    try:
        modal_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content .modal-title")))
    except Exception as e:
        print("ERROR:", str(e))

    proceed_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-content-btn a[href*='cart']")))
    driver.execute_script("arguments[0].click();", proceed_btn)
    time.sleep(1)
    save_html("cart_page")
    take_screenshot()

    second_checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary[href*='order']")))
    second_checkout_btn.click()
    time.sleep(1)
    save_html("address_form_page")
    take_screenshot()

    wait.until(EC.presence_of_element_located((By.ID, "field-id_country"))).click()
    driver.find_element(By.CSS_SELECTOR, "#field-id_country option[value='124']").click()
    driver.find_element(By.ID, "field-company").send_keys("CompTest")
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.ID, "field-address1")))
    driver.find_element(By.ID, "field-address1").send_keys("Street 1")
    time.sleep(3)
    driver.find_element(By.ID, "field-postcode").send_keys("LV-1234")
    driver.find_element(By.ID, "field-city").send_keys("Riga")
    driver.find_element(By.ID, "field-phone").send_keys("12345678")
    save_html("filled_address_form")
    take_screenshot()

    try:
        continue_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name='confirm-addresses']")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_btn)
        time.sleep(1)
        if continue_btn.is_enabled():
            driver.execute_script("arguments[0].click();", continue_btn)
        else:
            raise Exception("Button ERROR")
    except Exception as e:
        print("ERROR:", str(e))
        raise
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".delivery-options")))
    time.sleep(1)

    for i in range(3):
        try:
            my_carrier_radio = driver.find_element(By.ID, "delivery_option_2")
            driver.execute_script("arguments[0].scrollIntoView(true);", my_carrier_radio)
            time.sleep(1)
            my_carrier_radio.click()
            break
        except Exception as e:
            print(f"2 ERROR: {e}")
            time.sleep(2)

    save_html("delivery_option_page")
    take_screenshot()

    confirm_delivery_btn = wait.until(EC.element_to_be_clickable((By.NAME, "confirmDeliveryOption")))
    driver.execute_script("arguments[0].scrollIntoView(true);", confirm_delivery_btn)
    driver.execute_script("arguments[0].click();", confirm_delivery_btn)
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".payment-options")))

    cash_radio = wait.until(EC.element_to_be_clickable((By.ID, "payment-option-3")))
    driver.execute_script("arguments[0].scrollIntoView(true);", cash_radio)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", cash_radio)
    time.sleep(1)

    terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "conditions_to_approve[terms-and-conditions]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", terms_checkbox)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", terms_checkbox)
    place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#payment-payment-option-3-form button[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", place_order_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", place_order_button)

    save_html("order_confirmation")
    take_screenshot()

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN:: {output_file}")

finally:
    driver.quit()