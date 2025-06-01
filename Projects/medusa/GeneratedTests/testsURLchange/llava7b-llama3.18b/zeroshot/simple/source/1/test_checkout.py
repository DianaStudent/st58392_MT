import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        # Set up a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        # Clean up after each test runs (stop the browser)
        self.driver.quit()

    def test_checkout_process(self):
        # Add a product to cart
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']"))
        )
        add_to_cart_button.click()

        # Proceed to checkout from the shopping bag
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='cart']"))
        )
        cart_button.click()
        
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.HTML_DATA, "GO TO CHECKOUT"))
        )
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        email_field.send_keys("user@example.com")

        phone_number_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='phone']"))
        )
        phone_number_field.send_keys("+1234567890")

        shipping_address_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@name='address']"))
        )
        shipping_address_field.send_keys("123 Main St.")

        # Select shipping method
        shipping_method_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='shipping-method']"))
        )
        shipping_method_button.click()

        # Proceed to payment
        next_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.HTML_DATA, "Next"))
        )
        next_button.click()

        # Select payment method (assuming a credit card)
        payment_method_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='payment-method']"))
        )
        payment_method_button.click()

        # Confirm order
        confirm_order_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.HTML_DATA, "Confirm Order"))
        )
        confirm_order_button.click()

        # Verify final success page text
        self.assertEqual("Your order was placed successfully", WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='success-message']"))).text)

if __name__ == "__main__":
    unittest.main()