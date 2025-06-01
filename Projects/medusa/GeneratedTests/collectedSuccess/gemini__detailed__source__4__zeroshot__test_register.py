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
        self.first_name = "user"
        self.last_name = "test"
        self.password = "testuser"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the "Account" button in the right corner.
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        account_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(account_link_locator)
        )
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 3. Click the "Join us" button below the login form.
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(register_button_locator)
        )
        if register_button:
            register_button.click()
        else:
            self.fail("Join us button not found")

        # 4. Fill in all fields: first name, last name, email, and password.
        first_name_input_locator = (By.CSS_SELECTOR, '[data-testid="first-name-input"]')
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(first_name_input_locator)
        )
        if first_name_input:
            first_name_input.send_keys(self.first_name)
        else:
            self.fail("First name input not found")

        last_name_input_locator = (By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        last_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(last_name_input_locator)
        )
        if last_name_input:
            last_name_input.send_keys(self.last_name)
        else:
            self.fail("Last name input not found")

        email_input_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(email_input_locator)
        )
        if email_input:
            email_input.send_keys(self.email)
        else:
            self.fail("Email input not found")

        password_input_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(password_input_locator)
        )
        if password_input:
            password_input.send_keys(self.password)
        else:
            self.fail("Password input not found")

        # 5. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(submit_button_locator)
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 6. Verify registration success by checking presence of welcome message "Hello user".
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        welcome_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(welcome_message_locator)
        )
        if welcome_message:
            self.assertEqual(welcome_message.text, "Hello user")
        else:
            self.fail("Welcome message not found")

if __name__ == "__main__":
    unittest.main()