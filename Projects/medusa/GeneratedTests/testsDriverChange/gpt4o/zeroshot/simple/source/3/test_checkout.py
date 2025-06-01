import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_and_checkout(self):
        driver = self.driver

        # Open store page
        store_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Medusa Store")))
        store_link.click()

        # Click on a product link
        product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
        product_link.click()

        # Select size
        size_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Add to cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Go to cart
        cart_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_link.click()

        # Go to checkout
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        checkout_button.click()

        # Fill shipping info
        first_name_input = self.wait.until(EC.presence_of_element_located((By.NAME, "shipping_address.first_name")))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.NAME, "shipping_address.last_name")
        last_name_input.send_keys("test")

        address_input = driver.find_element(By.NAME, "shipping_address.address_1")
        address_input.send_keys("street 1")

        postal_code_input = driver.find_element(By.NAME, "shipping_address.postal_code")
        postal_code_input.send_keys("LV-1021")

        city_input = driver.find_element(By.NAME, "shipping_address.city")
        city_input.send_keys("Riga")

        country_select = driver.find_element(By.NAME, "shipping_address.country_code")
        country_select.send_keys("Denmark")

        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("user@test.com")

        # Continue to delivery
        continue_to_delivery_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # Select shipping method
        express_shipping_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Express Shipping']")))
        express_shipping_button.click()

        # Continue to payment
        continue_to_payment_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Select payment method
        manual_payment_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Manual Payment']")))
        manual_payment_button.click()

        # Continue to review
        continue_to_review_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Place order
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify order success
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your order was placed successfully')]")))
        self.assertIsNotNone(success_message, "Order completion text was not found.")

if __name__ == "__main__":
    unittest.main()