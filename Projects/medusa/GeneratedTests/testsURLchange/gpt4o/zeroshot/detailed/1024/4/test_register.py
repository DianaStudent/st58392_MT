import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8000/dk"
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage
        driver.get(self.base_url)

        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]')))
        account_button.click()

        # Step 3: Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="register-button"]')))
        join_us_button.click()

        # Step 4: Fill in registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="first-name-input"]')))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="last-name-input"]')))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]')))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]')))

        if not first_name_input or not last_name_input or not email_input or not password_input:
            self.fail("One or more registration form inputs are missing or not visible.")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        unique_email = f"user_{random.randint(1000, 9999)}@test.com"
        email_input.send_keys(unique_email)
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="register-button"]')))
        submit_button.click()

        # Step 6: Verify registration success
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]')))
            if not welcome_message or "Hello user" not in welcome_message.text:
                self.fail("Registration failed or welcome message not found.")
        except:
            self.fail("Welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()