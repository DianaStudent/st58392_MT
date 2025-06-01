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
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the account page
        try:
            account_link = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to click account link: {e}")

        # Click the register button
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']")))
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to click register button: {e}")

        # Fill in the registration form
        first_name = "user"
        last_name = "test"
        email = f"user_{uuid.uuid4().hex}@test.com"
        password = "testuser"

        try:
            first_name_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
            first_name_input.send_keys(first_name)
        except Exception as e:
            self.fail(f"Failed to fill first name: {e}")

        try:
            last_name_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']")))
            last_name_input.send_keys(last_name)
        except Exception as e:
            self.fail(f"Failed to fill last name: {e}")

        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            email_input.send_keys(email)
        except Exception as e:
            self.fail(f"Failed to fill email: {e}")

        try:
            phone_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='phone-input']")))
            phone_input.send_keys("12345678")
        except Exception as e:
            self.fail(f"Failed to fill phone: {e}")

        try:
            password_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))
            password_input.send_keys(password)
        except Exception as e:
            self.fail(f"Failed to fill password: {e}")

        # Submit the form
        try:
            register_submit_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']")))
            register_submit_button.click()
        except Exception as e:
            self.fail(f"Failed to submit registration: {e}")

        # Verify successful registration
        try:
            welcome_message = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertEqual(welcome_message.text, "Hello user")
        except Exception as e:
            self.fail(f"Registration failed: {e}")


if __name__ == "__main__":
    unittest.main()