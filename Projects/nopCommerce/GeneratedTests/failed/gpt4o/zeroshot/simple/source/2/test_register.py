from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver

        # Navigate to the registration page
        my_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        my_account_link.click()

        # Fill in registration form
        fake = Faker()
        email = fake.email()

        # First Name
        first_name = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        first_name.send_keys(fake.first_name())

        # Last Name
        last_name = driver.find_element(By.ID, "LastName")
        last_name.send_keys(fake.last_name())

        # Email
        email_field = driver.find_element(By.ID, "Email")
        email_field.send_keys(email)

        # Password
        password_field = driver.find_element(By.ID, "Password")
        password_field.send_keys("test11")

        # Confirm Password
        confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")
        confirm_password_field.send_keys("test11")

        # Submit the form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Check for success message
        success_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        self.assertIn("Your registration completed", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()