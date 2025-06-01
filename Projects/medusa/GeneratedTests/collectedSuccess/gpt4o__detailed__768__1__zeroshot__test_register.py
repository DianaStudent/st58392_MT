import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)
        
    def generate_email(self):
        """Generate a unique email address."""
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"user_{suffix}@test.com"

    def test_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Open the homepage and click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        if not account_button:
            self.fail("Account button not found")
        account_button.click()

        # Click the "Join Us" button to go to the registration page
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        if not join_us_button:
            self.fail("Join Us button not found")
        join_us_button.click()

        # Fill in the registration form
        email = self.generate_email()

        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        if not first_name_input:
            self.fail("First name input field not found")
        first_name_input.send_keys("user")

        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='last-name-input']")))
        if not last_name_input:
            self.fail("Last name input field not found")
        last_name_input.send_keys("test")

        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']")))
        if not email_input:
            self.fail("Email input field not found")
        email_input.send_keys(email)

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']")))
        if not password_input:
            self.fail("Password input field not found")
        password_input.send_keys("testuser")

        # Submit the registration form
        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='register-button']")))
        if not register_button:
            self.fail("Register button not found")
        register_button.click()

        # Verify registration success by checking welcome message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        if not welcome_message or "Hello user" not in welcome_message.text:
            self.fail("Welcome message not found or incorrect")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()