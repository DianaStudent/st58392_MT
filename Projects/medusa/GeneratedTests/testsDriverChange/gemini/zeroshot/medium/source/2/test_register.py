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
        self.email = f"user_{uuid.uuid4().hex}@test.com"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Click the "Account" link
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if account_link and account_link.text:
            account_link.click()
        else:
            self.fail("Account link not found or empty.")

        # 2. Click the "Join us" button
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if register_button and register_button.text == "Join us":
            register_button.click()
        else:
            self.fail("Join us button not found or text is incorrect.")

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

        if not all([first_name_input, last_name_input, email_input, password_input]):
            self.fail("One or more input fields not found.")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(self.email)
        password_input.send_keys("testuser")

        # 4. Submit the registration form
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if submit_button and submit_button.text == "Join":
            submit_button.click()
        else:
            self.fail("Register button not found or text is incorrect.")

        # 5. Verify registration success
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message and welcome_message.text:
            self.assertEqual(welcome_message.text, "Hello user")
        else:
            self.fail("Welcome message not found or empty.")

if __name__ == "__main__":
    unittest.main()