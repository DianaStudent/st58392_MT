from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to store
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-store-link"]')))
        store_link.click()

        # Select the sweatshirt product
        sweatshirt_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/dk/products/sweatshirt"]')))
        sweatshirt_link.click()

        # Select Size
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Add to cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        add_to_cart_button.click()

        # Go to cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # Proceed to checkout
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]')))
        go_to_checkout_button.click()

        # Fill in the address
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="shipping-first-name-input"]')))
        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-last-name-input"]')
        address_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-address-input"]')
        postal_code_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-postal-code-input"]')
        city_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-city-input"]')
        country_select = driver.find_element(By.CSS_SELECTOR, 'select[data-testid="shipping-country-select"]')
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-email-input"]')

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        address_input.send_keys("street 1")
        postal_code_input.send_keys("LV-1021")
        city_input.send_keys("Riga")
        country_select.send_keys("Denmark")
        email_input.send_keys("user@test.com")

        continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-address-button"]')
        continue_to_delivery_button.click()

        # Select delivery method
        delivery_method_radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="delivery-option-radio"]#headlessui-radio-:rh:')))
        delivery_method_radio.click()

        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-delivery-option-button"]')
        continue_to_payment_button.click()

        # Select payment method
        payment_method_radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span#headlessui-radio-:rk:')))
        payment_method_radio.click()

        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-payment-button"]')
        continue_to_review_button.click()

        # Confirm order
        place_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="submit-order-button"]')))
        place_order_button.click()

        # Verify success message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']")))
        self.assertIsNotNone(success_message, "Order success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()