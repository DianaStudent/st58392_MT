from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def get_element(self, by, value, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except:
            self.fail(f"Element with {by}: {value} not found or is empty.")

    def test_checkout_process(self):
        driver = self.driver

        # Step 2: Click on the menu button
        menu_button = self.get_element(By.ID, "headlessui-popover-button-:R6qdtt7:")
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = self.get_element(By.DATA_TEST_ID, "store-link")
        store_link.click()

        # Step 4: Click on a product image (thumbnail)
        product_thumbnail = self.get_element(By.CSS_SELECTOR, "img[alt='Thumbnail']")
        product_thumbnail.click()

        # Step 5: Select a size
        size_button = self.get_element(By.XPATH, "//button[text()='L']")
        size_button.click()

        # Step 6: Click the "Add to Cart" button
        add_to_cart_button = self.get_element(By.DATA_TEST_ID, "add-product-button")
        add_to_cart_button.click()

        # Step 7: Click the cart button to open the cart
        cart_button = self.get_element(By.DATA_TEST_ID, "nav-cart-link")
        cart_button.click()

        # Wait for presence of "GO TO CHECKOUT" button
        go_to_checkout_button = self.get_element(By.DATA_TEST_ID, "go-to-cart-button")
        go_to_checkout_button.click()

        # Step 8: Fill checkout fields
        self.get_element(By.DATA_TEST_ID, "shipping-first-name-input").send_keys("user")
        self.get_element(By.DATA_TEST_ID, "shipping-last-name-input").send_keys("test")
        self.get_element(By.DATA_TEST_ID, "shipping-address-input").send_keys("street 1")
        self.get_element(By.DATA_TEST_ID, "shipping-postal-code-input").send_keys("LV-1021")
        self.get_element(By.DATA_TEST_ID, "shipping-city-input").send_keys("Riga")

        country_select = self.get_element(By.DATA_TEST_ID, "shipping-country-select")
        country_select.click()
        country_select.send_keys("Denmark" + Keys.RETURN)

        self.get_element(By.DATA_TEST_ID, "shipping-email-input").send_keys("user@test.com")

        submit_address_button = self.get_element(By.DATA_TEST_ID, "submit-address-button")
        submit_address_button.click()

        # Step 9: Select delivery and payment methods
        delivery_radio_button = self.get_element(By.CSS_SELECTOR, "[data-testid='delivery-option-radio'] [type='button']")
        delivery_radio_button.click()

        continue_to_payment_button = self.get_element(By.DATA_TEST_ID, "submit-delivery-option-button")
        continue_to_payment_button.click()

        payment_radio_button = self.get_element(By.CSS_SELECTOR, "[data-testid='radio-button'][type='button']")
        payment_radio_button.click()

        continue_to_review_button = self.get_element(By.DATA_TEST_ID, "submit-payment-button")
        continue_to_review_button.click()

        # Step 10: Click "Place Order"
        place_order_button = self.get_element(By.DATA_TEST_ID, "submit-order-button")
        place_order_button.click()

        # Step 11: Verify order success message
        order_success_msg = self.get_element(By.XPATH, "//span[text()='Your order was placed successfully.']")
        self.assertIsNotNone(order_success_msg, "Order success message not found.")

if __name__ == "__main__":
    unittest.main()