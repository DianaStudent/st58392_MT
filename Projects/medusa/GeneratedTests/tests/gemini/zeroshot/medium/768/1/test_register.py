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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Click the "Account" link
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to click Account link: {e}")

        # 2. Click the "Join us" button
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to click Join us button: {e}")

        # 3. Fill in the registration form
        first_name = "user"
        last_name = "test"
        email = f"user_{uuid.uuid4().hex}@test.com"
        password = "testuser"

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
            )
            first_name_input.send_keys(first_name)

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
            )
            last_name_input.send_keys(last_name)

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys(email)

            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )
            password_input.send_keys(password)

        except Exception as e:
            self.fail(f"Failed to fill in registration form: {e}")

        # 4. Submit the registration form
        try:
            register_submit_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_submit_button.click()
        except Exception as e:
            self.fail(f"Failed to submit registration form: {e}")

        # 5. Verify registration success
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIsNotNone(welcome_message.text, "Welcome message is empty")
            self.assertTrue("Hello" in welcome_message.text, "Welcome message not found")
        except Exception as e:
            self.fail(f"Failed to verify registration success: {e}")


if __name__ == "__main__":
    unittest.main()