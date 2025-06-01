from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('data:text/html;charset=utf-8,' + html_data['home_before_register'])
        self.driver.maximize_window()

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10)) + '@example.com'

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to register page
        try:
            home_page = html_data['home_before_register']
            driver.get('data:text/html;charset=utf-8,' + home_page)
            account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
            account_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to account page: {e}")

        # Load register page directly for testing purposes
        register_page = html_data['register_page']
        driver.get('data:text/html;charset=utf-8,' + register_page)

        try:
            # Fill in registration form
            wait.until(EC.element_to_be_clickable((By.ID, "gender-male"))).click()
            wait.until(EC.element_to_be_clickable((By.ID, "FirstName"))).send_keys("John")
            wait.until(EC.element_to_be_clickable((By.ID, "LastName"))).send_keys("Doe")
            email = self.generate_random_email()
            wait.until(EC.element_to_be_clickable((By.ID, "Email"))).send_keys(email)
            wait.until(EC.element_to_be_clickable((By.ID, "Password"))).send_keys("test11")
            wait.until(EC.element_to_be_clickable((By.ID, "ConfirmPassword"))).send_keys("test11")

            # Submit registration form
            submit_button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            submit_button.click()
        except Exception as e:
            self.fail(f"Error during form filling or submission: {e}")

        # Confirm registration message
        register_result = html_data['register_result']
        driver.get('data:text/html;charset=utf-8,' + register_result)
        try:
            result_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
            self.assertEqual(result_message.text, "Your registration completed")
        except Exception as e:
            self.fail(f"Registration success message not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()