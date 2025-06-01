import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_checkout(self):
        # Login
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Your Email Address']"))
        )
        email_input.send_keys("test22@user.com")
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']"))
        )
        password_input.send_keys("test**11")
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        # Add products to cart
        product1_add_to_cart = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
        )
        product1_add_to_cart.click()
        product2_add_to_cart = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']")))
        product2_add_to_cart.click()

        # Go to cart page
        view_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']"))
        )
        view_cart_button.click()

        # Click "Proceed to Checkout"
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary proceed-to-checkout']"))
        )
        proceed_to_checkout_button.click()

        # Fill in the billing form
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='first_name']"))
        )
        last_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='last_name']"))
        )
        email_input_billing = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))
        )
        street_address_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='street_address']"))
        )
        apartment_suite_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='apartment_suite']"))
        )
        city_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='city']"))
        )
        state_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='state']"))
        )
        postal_code_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='postal_code']"))
        )

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        email_input_billing.clear()
        email_input_billing.send_keys("test22@user.com")
        street_address_input.send_keys("123 Street address My city, QC, CA H2H-2H2")
        apartment_suite_input.send_keys("101")
        city_input.send_keys("My City")
        state_input.send_keys("QC")
        postal_code_input.send_keys("H2H-2H2")

        # Confirm success by verifying that the billing form is filled
        self.assertEqual(first_name_input.get_attribute('value'), 'John')
        self.assertEqual(last_name_input.get_attribute('value'), 'Doe')
        self.assertEqual(email_input_billing.get_attribute('value'), 'test22@user.com')
        self.assertEqual(street_address_input.get_attribute('value'), '123 Street address My city, QC, CA H2H-2H2')
        self.assertEqual(apartment_suite_input.get_attribute('value'), '101')
        self.assertEqual(city_input.get_attribute('value'), 'My City')
        self.assertEqual(state_input.get_attribute('value'), 'QC')
        self.assertEqual(postal_code_input.get_attribute('value'), 'H2H-2H2')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()