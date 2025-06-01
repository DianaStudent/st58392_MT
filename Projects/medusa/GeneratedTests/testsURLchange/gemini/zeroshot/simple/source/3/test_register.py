import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the account page
        try:
            account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()
        except:
            self.fail("Account link not found or not clickable")

        # Navigate to the registration form
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']")))
            register_button.click()
        except:
            self.fail("Register button not found or not clickable")

        # Fill in the registration form
        first_name = "user"
        last_name = "test"
        email = f"user_{uuid.uuid4().hex}@test.com"
        password = "testuser"

        try:
            first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
            first_name_input.send_keys(first_name)
        except:
            self.fail("First name input not found")

        try:
            last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']")))
            last_name_input.send_keys(last_name)
        except:
            self.fail("Last name input not found")

        try:
            email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            email_input.send_keys(email)
        except:
            self.fail("Email input not found")

        try:
            phone_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='phone-input']")))
            phone_input.send_keys("1234567890")
        except:
            self.fail("Phone input not found")

        try:
            password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))
            password_input.send_keys(password)
        except:
            self.fail("Password input not found")

        # Submit the registration form
        try:
            register_submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']")))
            register_submit_button.click()
        except:
            self.fail("Register submit button not found or not clickable")

        # Verify successful registration
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertEqual(welcome_message.text, "Hello user")
        except:
            self.fail("Welcome message not found or incorrect")

if __name__ == "__main__":
    unittest.main()