from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Category A
        category_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        category_a_link.click()

        # Select Product A
        product_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product A")))
        product_a_link.click()

        # Add to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_button.click()

        # Click on cart button
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Go to checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT")))
        checkout_button.click()

        # Fill out checkout form
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")

        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Select shipping method
        shipping_method = driver.find_element(By.CSS_SELECTOR, ".shipping-methods input")
        shipping_method.click()

        # Select payment method
        payment_method = driver.find_element(By.CSS_SELECTOR, ".payment-methods input")
        payment_method.click()

        # Proceed to place order
        place_order_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap .button")
        place_order_button.click()

        # Confirm order success
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertIsNotNone(success_message, "Order success message was not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()