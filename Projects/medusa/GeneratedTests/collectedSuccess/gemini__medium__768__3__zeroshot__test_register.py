import unittest
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

        # 1. Click the "Account" link
        account_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 2. Click the "Join us" button
        register_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if register_button:
            register_button.click()
        else:
            self.fail("Register button not found")

        # 3. Fill in the registration form
        first_name_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
        )
        last_name_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
        )
        email_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        password_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )

        if not all([first_name_input, last_name_input, email_input, password_input]):
            self.fail("One or more input fields not found")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email = f"user_{uuid.uuid4().hex[:6]}@test.com"
        email_input.send_keys(email)
        password_input.send_keys("testuser")

        # 4. Submit the registration form
        submit_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 5. Verify registration success
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message and welcome_message.text:
            self.assertEqual("Hello user", welcome_message.text)
        else:
            self.fail("Welcome message not found or empty")


if __name__ == "__main__":
    unittest.main()