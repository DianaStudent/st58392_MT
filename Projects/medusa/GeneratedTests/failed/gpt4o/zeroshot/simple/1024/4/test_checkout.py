from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Store Page
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-store-link"]'))).click()

        # Add product to cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dk/products/sweatshirt"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="L"]'))).click()
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        if add_to_cart_button.text != "Add to cart":
            self.fail("Add to cart button is not available.")
        add_to_cart_button.click()

        # Go to Cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]'))).click()

        # Checkout
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]'))).click()

        # Fill in checkout details
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-email-input"]'))).send_keys("user@test.com")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-first-name-input"]'))).send_keys("user")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-last-name-input"]'))).send_keys("test")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-address-input"]'))).send_keys("street 1")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-postal-code-input"]'))).send_keys("LV-1021")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-city-input"]'))).send_keys("Riga")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[data-testid="shipping-country-select"]'))).send_keys("Denmark")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-address-button"]'))).click()

        # Choose delivery method
        wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Express Shipping"]/..'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-delivery-option-button"]'))).click()

        # Choose payment method
        wait.until(EC.element_to_be_clickable((By.XPATH, '//p[text()="Manual Payment"]/../..'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-payment-button"]'))).click()

        # Finalize order
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-order-button"]'))).click()

        # Verify success page
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Your order was placed successfully."]')))
        self.assertTrue(success_message.is_displayed(), "Success message is not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()