import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Set up Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "main")))
        except:
            self.fail("Home page did not load correctly.")

        # Step 2: Click the "Account" button in the right left corner
        try:
            account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_button.click()
        except:
            self.fail("Account button not found on home page.")

        # Step 3: Click the "Join Us" button below the login form
        try:
            join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
            join_us_button.click()
        except:
            self.fail("Join Us button not found on the login page.")

        # Step 4: Fill in all fields: first name, last name, and password from credentials, generate unique email
        first_name = "user"
        last_name = "test"
        email = f"user_{random.randint(1000, 9999)}@test.com"
        password = "testuser"

        try:
            first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
            last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
            email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")

            first_name_input.send_keys(first_name)
            last_name_input.send_keys(last_name)
            email_input.send_keys(email)
            password_input.send_keys(password)
        except:
            self.fail("Could not fill the registration form.")

        # Step 5: Submit the registration form
        try:
            register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
            register_button.click()
        except:
            self.fail("Register button not found or could not be clicked.")

        # Step 6: Verify registration success by checking the presence of welcome message "Hello user"
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except:
            self.fail("Welcome message 'Hello user' not found, registration might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()