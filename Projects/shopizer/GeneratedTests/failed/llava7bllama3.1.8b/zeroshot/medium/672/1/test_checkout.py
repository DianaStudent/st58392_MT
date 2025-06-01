from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        # Login to the website
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # Add product to the cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']"))
        )
        add_to_cart_button.click()

        # Open the cart and navigate to the cart page
        cart_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']"))
        )
        cart_link.click()

        # Click "Proceed to Checkout"
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-checkout']"))
        )
        proceed_to_checkout_button.click()

        # Fill in the billing form
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "first_name"))
        )
        last_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "last_name"))
        )
        address_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "address"))
        )

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        address_input.send_keys("123 Main St")

        # Accept terms and proceed
        terms_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
        )
        terms_checkbox.click()
        proceed_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-proceed']"))
        )
        proceed_button.click()

        # Confirm success by verifying that the billing form is filled
        self.assertEqual(first_name_input.get_attribute("value"), "John")
        self.assertEqual(last_name_input.get_attribute("value"), "Doe")
        self.assertEqual(address_input.get_attribute("value"), "123 Main St")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()