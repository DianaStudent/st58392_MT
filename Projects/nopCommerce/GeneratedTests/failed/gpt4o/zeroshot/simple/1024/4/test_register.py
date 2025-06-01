from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_random_email(self):
        return 'user_' + ''.join(random.choice(string.ascii_letters) for _ in range(10)) + '@test.com'

    def test_registration(self):
        driver = self.driver

        # Navigate to the registration page
        my_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        my_account_link.click()
        
        # Fill the registration form
        first_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "FirstName")))
        last_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "LastName")))
        email_input = self.wait.until(EC.element_to_be_clickable((By.ID, "Email")))
        password_input = self.wait.until(EC.element_to_be_clickable((By.ID, "Password")))
        confirm_password_input = self.wait.until(EC.element_to_be_clickable((By.ID, "ConfirmPassword")))
        female_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "register-button")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys(self.generate_random_email())
        password_input.send_keys("test11")
        confirm_password_input.send_keys("test11")
        female_radio.click()
        
        # Submit the registration form
        register_button.click()

        # Verify registration success
        result_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        self.assertIn("Your registration completed", result_message.text, "Registration failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()