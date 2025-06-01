from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to the store page
        store_link = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='nav-store-link']")
        store_link.click()

        # Choose a product and go to product page
        product = self.wait_for_element(By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")
        product.click()

        # Select size and add to cart
        size_button = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='option-button']")
        size_button.click()

        add_to_cart_button = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='add-product-button']")
        add_to_cart_button.click()

        # Go to cart
        cart_link = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='nav-cart-link']")
        cart_link.click()

        # Go to checkout
        go_to_cart_button = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='go-to-cart-button']")
        go_to_cart_button.click()

        # Fill shipping address
        self.fill_input("[data-testid='shipping-first-name-input']", "user")
        self.fill_input("[data-testid='shipping-last-name-input']", "test")
        self.fill_input("[data-testid='shipping-address-input']", "street 1")
        self.fill_input("[data-testid='shipping-postal-code-input']", "LV-1021")
        self.fill_input("[data-testid='shipping-city-input']", "Riga")
        email_input = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='shipping-email-input']")
        email_input.clear()
        email_input.send_keys("user@test.com")

        continue_to_delivery_button = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # Choose delivery method and continue to payment
        delivery_radio_button = self.wait_for_element(By.CSS_SELECTOR, "span[id^='headlessui-radio-']")
        delivery_radio_button.click()

        continue_to_payment_button = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Choose payment method and continue to review
        payment_radio_button = self.wait_for_element(By.CSS_SELECTOR, "span[id^='headlessui-radio-']")
        payment_radio_button.click()

        continue_to_review_button = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Place order
        place_order_button = self.wait_for_element(By.CSS_SELECTOR, "[data-testid='submit-order-button']")
        place_order_button.click()

        # Confirm success message
        success_message = self.wait_for_element(By.CSS_SELECTOR, "span:contains('Your order was placed successfully')")
        if not success_message:
            self.fail("Order success message not found.")

    def wait_for_element(self, by, value):
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except:
            self.fail(f"Element with {by}='{value}' not found.")

    def fill_input(self, selector, value):
        input_field = self.wait_for_element(By.CSS_SELECTOR, selector)
        input_field.clear()
        input_field.send_keys(value)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()