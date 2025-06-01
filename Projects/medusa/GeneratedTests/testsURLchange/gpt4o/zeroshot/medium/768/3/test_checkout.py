import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Open home page and click on the menu button
        menu_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]'))
        )
        menu_button.click()

        # Step 2: Click on the "Store" link
        store_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]'))
        )
        store_link.click()

        # Step 3: Click on a product image (thumbnail)
        product_thumbnail = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li:first-child a'))
        )
        product_thumbnail.click()

        # Step 4: Select a size
        size_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="option-button"]'))
        )
        size_option.click()

        # Step 5: Click the "Add to Cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]'))
        )
        add_to_cart_button.click()

        # Step 6: Click the cart button to open the cart
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]'))
        )
        cart_button.click()

        # Step 7: Click "Go to checkout"
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]'))
        )
        go_to_checkout_button.click()

        # Step 8: Fill checkout fields
        self.fill_checkout_fields(driver)

        # Step 9: Select delivery and payment methods
        self.select_delivery_and_payment_methods(driver)
        
        # Step 10: Click "Place Order"
        place_order_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="submit-order-button"]'))
        )
        place_order_button.click()

        # Step 11: Verify the confirmation page contains success message
        self.verify_order_success(driver)

    def fill_checkout_fields(self, driver):
        field_ids = {
            "shipping-first-name-input": "user",
            "shipping-last-name-input": "test",
            "shipping-address-input": "street 1",
            "shipping-postal-code-input": "LV-1021",
            "shipping-city-input": "Riga",
            "shipping-country-select": "dk",
            "shipping-email-input": "user@test.com"
        }

        for field_id, value in field_ids.items():
            field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f'input[data-testid="{field_id}"], select[data-testid="{field_id}"]'))
            )
            if field.tag_name == 'select':
                field.click()
                option = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, f'select[data-testid="{field_id}"] option[value="{value}"]'))
                )
                option.click()
            else:
                field.send_keys(value)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-address-button"]')
        submit_button.click()

    def select_delivery_and_payment_methods(self, driver):
        # Assuming two options for demonstration, choose the first available option
        delivery_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="delivery-option-radio"] button'))
        )
        delivery_option.click()

        submit_delivery_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-delivery-option-button"]')
        submit_delivery_button.click()

        payment_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[id^="headlessui-radio-"] button'))
        )
        payment_option.click()

        submit_payment_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-payment-button"]')
        submit_payment_button.click()

    def verify_order_success(self, driver):
        confirmation_text_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="order-complete-container"] h1'))
        )
        self.assertTrue("Your order was placed successfully" in confirmation_text_element.text, 
                        "The success message was not found!")

if __name__ == "__main__":
    unittest.main()