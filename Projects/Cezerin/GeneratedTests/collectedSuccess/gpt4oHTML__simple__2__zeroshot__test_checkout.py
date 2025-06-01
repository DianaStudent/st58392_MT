import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost:3000/')  # Adjust the file path according to your local setup

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to Product A page
        product_a_link = driver.find_element(By.XPATH, "//a[@href='/category-a/product-a']")
        product_a_link.click()

        # Wait and Click Add to Cart Button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Wait for the mini cart to be available and click 'Go to checkout'
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Go to checkout']")))
        go_to_checkout_button.click()

        # Fill in Customer Details
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")

        mobile_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer.mobile")))
        mobile_input.send_keys("12345678")

        state_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "shipping_address.state")))
        state_input.send_keys("Riga")

        city_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "shipping_address.city")))
        city_input.send_keys("Riga")

        # Select Shipping Method
        shipping_method = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='shipping_method_id']")))
        shipping_method.click()

        # Select Payment Method
        payment_method = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='payment_method_id']")))
        payment_method.click()

        # Click the Next Button to finalize.
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
        next_button.click()

        # Place Order Button
        place_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Confirm Order Success
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))

        self.assertIsNotNone(success_message, "Order was not completed successfully, expected success message not found.")

if __name__ == "__main__":
    unittest.main()