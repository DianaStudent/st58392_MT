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
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        # Login
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "email")))
        email_input.send_keys("test22@user.com")
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))
        password_input.send_keys("test**11")
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()

        # Add products to cart
        add_product_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "add-to-cart")))
        add_product_button.click()

        # Go to cart page
        view_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']")))
        view_cart_button.click()

        # Proceed to Checkout
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "proceed-to-checkout")))
        proceed_to_checkout_button.click()

        # Fill in billing form
        first_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "first-name")))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "last-name")))
        address1_input = WebDriverWait(self.driver, 20).until(EC.element_to.be_clickable((By.ID, "address-1")))
        city_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "city")))
        state_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "state")))
        zip_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "zip-code")))
        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        address1_input.send_keys("123 Main St")
        city_input.send_keys("Anytown")
        state_input.send_keys("CA")
        zip_code_input.send_keys("12345")

        # Confirm success by verifying that the billing form is filled
        self.assertTrue(first_name_input.get_attribute("value") == "John")
        self.assertTrue(last_name_input.get_attribute("value") == "Doe")
        self.assertTrue(address1_input.get_attribute("value") == "123 Main St")
        self.assertTrue(city_input.get_attribute("value") == "Anytown")
        self.assertTrue(state_input.get_attribute("value") == "CA")
        self.assertTrue(zip_code_input.get_attribute("value") == "12345")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()