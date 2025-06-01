import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

process_name = "checkout"
base_dir = r"C:\Diana\MasterCode\code\Projects\medusa\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

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

    menu_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='nav-menu-button']")
    menu_button.click()
    time.sleep(1)
    save_html("menu_opened")

    store_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='store-link']")
    store_link.click()
    time.sleep(2)
    save_html("store_page")

    product_image = driver.find_element(By.CSS_SELECTOR, "img[alt='Thumbnail']")
    product_image.click()
    time.sleep(2)
    save_html("product_page")

    size_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='option-button']")
    size_button.click()
    time.sleep(1)
    save_html("size_selected")

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='add-product-button']")
    add_to_cart_button.click()
    time.sleep(2)
    save_html("product_added")

    cart_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='nav-cart-link']")
    cart_link.click()
    time.sleep(2)
    save_html("cart_page")

    checkout_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='checkout-button']")
    checkout_button.click()
    time.sleep(2)
    save_html("checkout_address_page")

    driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-first-name-input']").send_keys("user")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-last-name-input']").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-address-input']").send_keys("street 1")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-city-input']").send_keys("Riga")
    country_select = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-country-select']")
    country_select.send_keys("Denmark")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-email-input']").send_keys("user@test.com")
    time.sleep(1)
    save_html("address_filled")

    submit_address_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-address-button']")
    submit_address_button.click()
    time.sleep(2)
    save_html("delivery_options")

    delivery_option = driver.find_element(By.CSS_SELECTOR, "[data-testid='delivery-option-radio']")
    delivery_option.click()
    time.sleep(1)
    save_html("delivery_selected")

    continue_to_payment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='submit-delivery-option-button']"))
    )
    continue_to_payment_button.click()
    time.sleep(2)
    save_html("payment_options")

    payment_option = driver.find_element(By.CSS_SELECTOR, "[data-testid='radio-button']")
    payment_option.click()
    time.sleep(1)
    save_html("payment_selected")

    continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-payment-button']")
    continue_to_review_button.click()
    time.sleep(2)
    save_html("review_page")

    place_order_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-order-button']")
    place_order_button.click()
    time.sleep(3)
    save_html("order_complete")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
