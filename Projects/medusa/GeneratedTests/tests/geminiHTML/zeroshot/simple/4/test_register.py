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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        try:
            # Navigate to the account page
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()

            # Click the register button
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_button.click()

            # Fill in the registration form
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
            )
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
            )
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            phone_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='phone-input']"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )
            register_submit_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )

            email = f"user_{uuid.uuid4().hex}@test.com"

            first_name_input.send_keys("user")
            last_name_input.send_keys("test")
            email_input.send_keys(email)
            phone_input.send_keys("123-456-7890")
            password_input.send_keys("testuser")
            register_submit_button.click()

            # Verify successful registration
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertEqual(welcome_message.text, "Hello user")

        except Exception as e:
            self.fail(f"An error occurred: {e}")


if __name__ == "__main__":
    unittest.main()