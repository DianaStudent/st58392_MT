import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Open the account page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Click the "Join Us" button
        join_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        join_button.click()

        # Fill in the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        if not first_name_input:
            self.fail("First name input is missing!")
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        if not last_name_input:
            self.fail("Last name input is missing!")
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        if not email_input:
            self.fail("Email input is missing!")
        unique_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(unique_email)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        if not password_input:
            self.fail("Password input is missing!")
        password_input.send_keys("testuser")

        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        if not register_button:
            self.fail("Register button is missing!")
        register_button.click()

        # Verify registration success by checking the presence of the welcome message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        if not welcome_message.text.strip():
            self.fail("Welcome message is not present or empty!")
        
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()