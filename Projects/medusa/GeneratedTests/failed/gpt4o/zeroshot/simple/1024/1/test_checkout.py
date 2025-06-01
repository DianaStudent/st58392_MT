from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Add product to cart
        driver.get("http://localhost:8000/dk/store")
        product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/dk/products/sweatshirt')]")))
        product_link.click()

        # Select size and add to cart
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Go to cart
        cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_link.click()

        # Go to checkout
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill out the shipping address
        first_name_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-first-name-input']")))
        first_name_input.send_keys("user")
        last_name_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-last-name-input']")
        last_name_input.send_keys("test")
        address_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-address-input']")
        address_input.send_keys("street 1")
        postal_code_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-postal-code-input']")
        postal_code_input.send_keys("LV-1021")
        city_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-city-input']")
        city_input.send_keys("Riga")
        country_select = driver.find_element(By.XPATH, "//select[@data-testid='shipping-country-select']")
        country_select.send_keys("Denmark")
        email_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-email-input']")
        email_input.send_keys("user@test.com")

        # Continue to delivery
        continue_to_delivery_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # Select delivery option
        delivery_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio']")))
        delivery_option.click()

        # Continue to payment
        continue_to_payment_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Select payment method
        payment_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='radio-button']")))
        payment_option.click()

        # Continue to review
        continue_to_review_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Place order
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify order completion
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']")))
        self.assertIsNotNone(success_message, "Order not placed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()