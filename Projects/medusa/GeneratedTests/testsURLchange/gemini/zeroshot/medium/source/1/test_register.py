import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)
        self.email = f"user_{uuid.uuid4().hex}@test.com"
        self.firstname = "user"
        self.lastname = "test"
        self.password = "testuser"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Click the "Account" link
        account_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 2. Click the "Join us" button
        join_us_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if join_us_button:
            join_us_button.click()
        else:
            self.fail("Join us button not found")

        # 3. Fill in the registration form
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
        )
        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
        )
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )

        if first_name_input and last_name_input and email_input and password_input:
            first_name_input.send_keys(self.firstname)
            last_name_input.send_keys(self.lastname)
            email_input.send_keys(self.email)
            password_input.send_keys(self.password)
        else:
            self.fail("One or more input fields not found")

        # 4. Submit the registration form
        register_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if register_button:
            register_button.click()
        else:
            self.fail("Register button not found")

        # 5. Verify registration success
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message:
            self.assertTrue(welcome_message.is_displayed(), "Welcome message is not displayed")
            self.assertIn("Hello", welcome_message.text, "Welcome message does not contain 'Hello'")
        else:
            self.fail("Welcome message not found")


if __name__ == "__main__":
    unittest.main()