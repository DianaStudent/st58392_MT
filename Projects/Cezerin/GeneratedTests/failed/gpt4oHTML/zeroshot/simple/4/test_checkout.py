from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Category A Page
        category_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        category_a_link.click()

        # Select Product A
        product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product A")))
        product_link.click()

        # Add Product to Cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-addtocart")))
        add_to_cart_button.click()

        # Click on the Cart Button
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Go to Checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout")))
        checkout_button.click()

        # Fill in Checkout Details
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")

        mobile_input = wait.until(EC.element_to_be_clickable((By.ID, "customer.mobile")))
        mobile_input.send_keys("12345678")

        state_input = wait.until(EC.element_to_be_clickable((By.ID, "shipping_address.state")))
        state_input.send_keys("Riga")

        city_input = wait.until(EC.element_to_be_clickable((By.ID, "shipping_address.city")))
        city_input.send_keys("Riga")

        # Select Shipping Method
        shipping_method = wait.until(EC.presence_of_element_located((By.NAME, "shipping_method_id")))
        shipping_method.click()

        # Select Payment Method
        payment_method = wait.until(EC.presence_of_element_located((By.NAME, "payment_method_id")))
        payment_method.click()

        # Place Order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
        place_order_button.click()

        # Confirm Success Message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()