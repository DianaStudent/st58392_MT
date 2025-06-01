from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerce(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_ecommerce_flow(self):
        # Open the home page
        self.driver.get("http://localhost/")

        # Log in using the provided credentials
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # Add product to the cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary add-to-cart']")))
        add_to_cart_button.click()

        # Open the cart and navigate to the cart page
        cart_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']")))
        cart_link.click()

        # Click "Proceed to Checkout"
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary checkout-button']")))
        proceed_to_checkout_button.click()

        # Fill in the billing form
        first_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "first_name")))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "last_name")))
        email_input_billing = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email")))
        address_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "address")))
        city_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "city")))
        state_select = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "state")))
        country_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "country")))
        zip_code_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "zip_code")))

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        email_input_billing.clear()
        email_input_billing.send_keys("test22@user.com")
        address_input.send_keys("123 Main St")
        city_input.send_keys("New York")
        state_select.click()  # Wait for select to appear
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='NY']"))).click()
        country_input.send_keys("USA")
        zip_code_input.send_keys("10001")

        # Accept terms and proceed
        terms_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "terms")))
        terms_checkbox.click()
        accept_terms_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary accept-terms']")))
        accept_terms_button.click()

        # Confirm success if form is filled
        self.assertTrue(first_name_input.get_attribute("value") == "John")
        self.assertTrue(last_name_input.get_attribute("value") == "Doe")
        self.assertTrue(email_input_billing.get_attribute("value") == "test22@user.com")
        self.assertTrue(address_input.get_attribute("value") == "123 Main St")
        self.assertTrue(city_input.get_attribute("value") == "New York")
        self.assertTrue(state_select.get_attribute("value") == "NY")
        self.assertTrue(country_input.get_attribute("value") == "USA")
        self.assertTrue(zip_code_input.get_attribute("value") == "10001")

if __name__ == '__main__':
    unittest.main()