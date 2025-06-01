import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to Category A
        category_a = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
        category_a.click()

        # Select Product A
        product_a = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
        product_a.click()

        # Add product to cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Click on cart button
        cart_button = driver.find_element(By.CSS_SELECTOR, ".cart-button")
        cart_button.click()

        # Wait for and click on "GO TO CHECKOUT" button
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Go to checkout']")))
        go_to_checkout_button.click()

        # Fill in checkout details
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")

        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")

        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Choose shipping method
        shipping_method = driver.find_element(By.NAME, "shipping_method_id")
        shipping_method.click()

        # Choose payment method
        payment_method = driver.find_element(By.NAME, "payment_method_id")
        payment_method.click()

        # Click on Next button
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button")
        next_button.click()

        # Place the order
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Confirm the success message
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertTrue(success_message, "Order was not successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()