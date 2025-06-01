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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.url = "http://localhost:8000/dk"
        self.first_name = "user"
        self.last_name = "test"
        self.password = "testuser"
        self.email = f"user_{uuid.uuid4().hex}@test.com"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Open the homepage.
        # 2. Click the "Account" button in the right left corner.
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(account_link_locator)
        )
        account_link.click()

        # 3. Click the "Join Us" button below the login form.
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(register_button_locator)
        )
        register_button.click()

        # 4. Fill in all fields: first name, last name, and password from credentials, generate unique email.
        first_name_input_locator = (By.CSS_SELECTOR, '[data-testid="first-name-input"]')
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(first_name_input_locator)
        )
        first_name_input.send_keys(self.first_name)

        last_name_input_locator = (By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(last_name_input_locator)
        )
        last_name_input.send_keys(self.last_name)

        email_input_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_input_locator)
        )
        email_input.send_keys(self.email)

        password_input_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(password_input_locator)
        )
        password_input.send_keys(self.password)

        # 5. Submit the registration form.
        register_submit_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(register_submit_button_locator)
        )
        register_submit_button.click()

        # 6. Verify registration success by checking presence of welcome message "Hello user".
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(welcome_message_locator)
        )

        welcome_message_text = welcome_message.get_attribute('data-value')
        self.assertEqual(welcome_message_text, self.first_name, "Registration failed. Welcome message not found.")


if __name__ == "__main__":
    unittest.main()