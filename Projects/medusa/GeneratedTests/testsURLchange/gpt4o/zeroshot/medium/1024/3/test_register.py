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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def generate_unique_email(self):
        """Generate a unique email using the current time."""
        return f"user_{int(time.time())}@test.com"

    def test_registration(self):
        driver = self.driver
        
        # Step 1: Open the homepage
        driver.get("http://localhost:8000/dk")
        
        # Step 2: Click the "Account" link
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-account-link']"))
            )
            account_link.click()
        except:
            self.fail("Account link not found or not clickable.")

        # Step 3: Click the "Join Us" button
        try:
            join_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[@data-testid='register-button']"))
            )
            join_button.click()
        except:
            self.fail("Join Us button not found or not clickable.")

        # Step 4: Fill in all fields
        first_name = "user"
        last_name = "test"
        email = self.generate_unique_email()
        password = "testuser"
        
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-testid='first-name-input']"))
            )
            first_name_input.send_keys(first_name)
        except:
            self.fail("First name input not found or not fillable.")

        try:
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-testid='last-name-input']"))
            )
            last_name_input.send_keys(last_name)
        except:
            self.fail("Last name input not found or not fillable.")

        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-testid='email-input']"))
            )
            email_input.send_keys(email)
        except:
            self.fail("Email input not found or not fillable.")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-testid='password-input']"))
            )
            password_input.send_keys(password)
        except:
            self.fail("Password input not found or not fillable.")

        # Step 5: Submit the registration form
        try:
            submit_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[@data-testid='register-button' and @type='submit']"))
            )
            submit_button.click()
        except:
            self.fail("Submit button not found or not clickable.")

        # Step 6: Verify registration success by checking presence of welcome message
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[@data-testid='welcome-message']"))
            )
            self.assertTrue(welcome_message.is_displayed(), "Welcome message is not displayed.")
        except:
            self.fail("Registration not successful, welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()