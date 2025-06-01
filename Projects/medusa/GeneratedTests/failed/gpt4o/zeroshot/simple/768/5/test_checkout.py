from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to store and select product
        store_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-store-link']"))
        )
        store_link.click()

        product_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
        )
        product_link.click()

        # Select size
        size_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='L']"))
        )
        size_button.click()

        # Add product to cart
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # Go to cart
        cart_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
        )
        cart_link.click()

        # Proceed to checkout
        go_to_checkout_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))
        )
        go_to_checkout_button.click()

        # Fill shipping address
        first_name_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
        )
        first_name_input.send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
        country_dropdown = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
        country_dropdown.click()
        driver.find_element(By.CSS_SELECTOR, "option[value='dk']").click()
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")

        continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # Select delivery method
        express_shipping = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rh:'] button[data-testid='radio-button']"))
        )
        express_shipping.click()

        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Select payment method
        manual_payment = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:'] button[data-testid='radio-button']"))
        )
        manual_payment.click()

        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Place order
        place_order_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
        )
        place_order_button.click()

        # Verify order completion
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']"))
        )
        self.assertIsNotNone(success_message, "Order completion message not found!")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()