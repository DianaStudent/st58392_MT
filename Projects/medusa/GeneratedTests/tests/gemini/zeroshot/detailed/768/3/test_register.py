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
        self.credentials = {
            "first_name": "user",
            "last_name": "test",
            "email": f"user_{uuid.uuid4().hex}@test.com",
            "password": "testuser"
        }

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the "Account" button in the right corner.
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        account_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located(account_link_locator))
        account_link.click()

        # 3. Click the "Join us" button below the login form.
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(register_button_locator))
        register_button.click()

        # 4. Fill in all fields: first name, last name, email and password.
        first_name_input_locator = (By.CSS_SELECTOR, '[data-testid="first-name-input"]')
        first_name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(first_name_input_locator))
        first_name_input.send_keys(self.credentials["first_name"])

        last_name_input_locator = (By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        last_name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(last_name_input_locator))
        last_name_input.send_keys(self.credentials["last_name"])

        email_input_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        email_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(email_input_locator))
        email_input.send_keys(self.credentials["email"])

        password_input_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(password_input_locator))
        password_input.send_keys(self.credentials["password"])

        # 5. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        submit_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(submit_button_locator))
        submit_button.click()

        # 6. Verify registration success by checking presence of welcome message "Hello user".
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        welcome_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located(welcome_message_locator))

        if welcome_message and welcome_message.text:
            self.assertEqual(welcome_message.text, "Hello user")
        else:
            self.fail("Welcome message is not present or empty.")

if __name__ == "__main__":
    unittest.main()