import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/")

    def tearDown(self):
        self.driver.quit()

    def test_checkout(self):
        # Add product to cart
        add_product_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']")))
        add_product_button.click()

        # Click on cart button and go to checkout
        cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//a[@class='cart'])[1]")))
        cart_button.click()
        checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='GO TO CHECKOUT']")))
        checkout_button.click()

        # Fill required checkout fields
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys("test@example.com")

        phone_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "phone")))
        phone_field.send_keys("1234567890")

        shipping_address_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "shippingAddress")))
        shipping_address_field.send_keys("Test Shipping Address")

        # Select shipping method
        shipping_method_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='shippingMethod']")))
        shipping_method_dropdown.click()
        shipping_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//option)[1]")))
        shipping_option.click()

        # Select payment method
        payment_method_dropdown = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='paymentMethod']")))
        payment_method_dropdown.click()
        payment_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//option)[1]")))
        payment_option.click()

        # Place order
        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Confirm final success page contains "Thanks for your order!"
        success_page_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Thanks for your order!']")))
        self.assertTrue(success_page_text.is_displayed())

if __name__ == "__main__":
    unittest.main()