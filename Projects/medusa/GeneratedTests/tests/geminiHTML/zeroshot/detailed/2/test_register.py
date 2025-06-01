import unittest
import time
import uuid

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the "Account" button in the right corner.
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        account_link = self.wait.until(EC.presence_of_element_located(account_link_locator))
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 3. Click the "Join us" button below the login form.
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_button = self.wait.until(EC.presence_of_element_located(register_button_locator))
        if register_button:
            register_button.click()
        else:
            self.fail("Join us button not found")

        # 4. Fill in all fields: first name, last name, email, and password.
        first_name_locator = (By.CSS_SELECTOR, '[data-testid="first-name-input"]')
        last_name_locator = (By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        email_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        phone_locator = (By.CSS_SELECTOR, '[data-testid="phone-input"]')
        password_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')

        first_name_input = self.wait.until(EC.presence_of_element_located(first_name_locator))
        last_name_input = self.wait.until(EC.presence_of_element_located(last_name_locator))
        email_input = self.wait.until(EC.presence_of_element_located(email_locator))
        phone_input = self.wait.until(EC.presence_of_element_located(phone_locator))
        password_input = self.wait.until(EC.presence_of_element_located(password_locator))
        register_button = self.wait.until(EC.presence_of_element_located(register_button_locator))

        if not all([first_name_input, last_name_input, email_input, password_input]):
            self.fail("One or more input fields not found")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(f"user_{uuid.uuid4().hex}@test.com")
        phone_input.send_keys("1234567890")
        password_input.send_keys("testuser")

        # 5. Submit the registration form.
        register_button = self.wait.until(EC.element_to_be_clickable(register_button_locator))
        if register_button:
            register_button.click()
        else:
            self.fail("Register button not found or not clickable")

        # 6. Verify registration success by checking presence of welcome message "Hello user".
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        welcome_message = self.wait.until(EC.presence_of_element_located(welcome_message_locator))

        if welcome_message:
            self.assertEqual(welcome_message.text, "Hello user", "Welcome message is incorrect")
        else:
            self.fail("Welcome message not found")

if __name__ == "__main__":
    unittest.main()