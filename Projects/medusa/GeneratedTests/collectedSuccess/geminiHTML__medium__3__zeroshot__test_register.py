import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)
        self.email = f"user_{int(time.time())}@test.com"
        self.first_name = "user"
        self.last_name = "test"
        self.password = "testuser"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Click the "Account" link.
        account_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_link.click()

        # 3. Click the "Join us" button.
        register_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        register_button.click()

        # 4. Fill in all fields: first name, last name, email, password.
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
        )
        first_name_input.send_keys(self.first_name)

        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
        )
        last_name_input.send_keys(self.last_name)

        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        email_input.send_keys(self.email)

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )
        password_input.send_keys(self.password)

        # 5. Submit the registration form.
        register_submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        register_submit_button.click()

        # 6. Verify registration success by checking presence of welcome message.
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIsNotNone(welcome_message, "Welcome message not found after registration.")
            self.assertNotEqual(welcome_message.text, "", "Welcome message is empty.")
        except Exception as e:
            self.fail(f"Failed to verify registration success: {e}")

if __name__ == "__main__":
    unittest.main()