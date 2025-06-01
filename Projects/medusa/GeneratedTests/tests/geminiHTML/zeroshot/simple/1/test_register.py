import unittest
import time
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to account page
        try:
            account_link = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Account link not found or not clickable: {e}")

        # Click register button
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found or not clickable: {e}")

        # Fill in registration form
        first_name = "user"
        last_name = "test"
        email = f"user_{uuid.uuid4().hex}@test.com"
        password = "testuser"
        phone = "1234567890"

        try:
            first_name_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
            )
            first_name_input.send_keys(first_name)
        except Exception as e:
            self.fail(f"First name input not found: {e}")

        try:
            last_name_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
            )
            last_name_input.send_keys(last_name)
        except Exception as e:
            self.fail(f"Last name input not found: {e}")

        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys(email)
        except Exception as e:
            self.fail(f"Email input not found: {e}")

        try:
            phone_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='phone-input']"))
            )
            phone_input.send_keys(phone)
        except Exception as e:
            self.fail(f"Phone input not found: {e}")

        try:
            password_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )
            password_input.send_keys(password)
        except Exception as e:
            self.fail(f"Password input not found: {e}")

        # Submit registration form
        try:
            register_submit_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_submit_button.click()
        except Exception as e:
            self.fail(f"Register submit button not found or not clickable: {e}")

        # Verify registration success
        try:
            welcome_message = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertEqual(welcome_message.get_attribute("data-value"), first_name, "Welcome message is incorrect.")
        except Exception as e:
            self.fail(f"Welcome message not found: {e}")


if __name__ == "__main__":
    unittest.main()