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
        # 1. Open the homepage.
        # 2. Click the "Account" button in the right left corner.
        account_link_locator = (By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(account_link_locator)
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to click account link: {e}")

        # 3. Click the "Join Us" button below the login form.
        register_button_locator = (By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(register_button_locator)
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to click register button: {e}")

        # 4. Fill in all fields: first name, last name, and password from credentials, generate unique email.
        first_name_locator = (By.CSS_SELECTOR, 'input[data-testid="first-name-input"]')
        last_name_locator = (By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        email_locator = (By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        password_locator = (By.CSS_SELECTOR, 'input[data-testid="password-input"]')

        first_name = "user"
        last_name = "test"
        email = f"user_{uuid.uuid4().hex}@test.com"
        password = "testuser"

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(first_name_locator)
            )
            first_name_input.send_keys(first_name)

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(last_name_locator)
            )
            last_name_input.send_keys(last_name)

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(email_locator)
            )
            email_input.send_keys(email)

            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(password_locator)
            )
            password_input.send_keys(password)

        except Exception as e:
            self.fail(f"Failed to fill form fields: {e}")

        # 5. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        try:
            submit_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(submit_button_locator)
            )
            submit_button.click()
        except Exception as e:
            self.fail(f"Failed to submit the form: {e}")

        # 6. Verify registration success by checking presence of welcome message "Hello user".
        welcome_message_locator = (By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(welcome_message_locator)
            )
            self.assertEqual("Hello user", welcome_message.text)
        except Exception as e:
            self.fail(f"Failed to verify registration: {e}")


if __name__ == "__main__":
    unittest.main()