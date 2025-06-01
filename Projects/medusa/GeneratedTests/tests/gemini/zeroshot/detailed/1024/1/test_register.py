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

    def test_registration(self):
        driver = self.driver
        email = f"user_{uuid.uuid4().hex}@test.com"
        first_name = "user"
        last_name = "test"
        password = "testuser"

        # 1. Click the "Account" button
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(account_link_locator)
        )
        account_link.click()

        # 2. Click the "Join us" button
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(register_button_locator)
        )
        register_button.click()

        # 3. Fill in the registration form
        first_name_input_locator = (By.CSS_SELECTOR, '[data-testid="first-name-input"]')
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(first_name_input_locator)
        )
        first_name_input.send_keys(first_name)

        last_name_input_locator = (By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(last_name_input_locator)
        )
        last_name_input.send_keys(last_name)

        email_input_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_input_locator)
        )
        email_input.send_keys(email)

        phone_input_locator = (By.CSS_SELECTOR, '[data-testid="phone-input"]')
        phone_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(phone_input_locator)
        )

        password_input_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(password_input_locator)
        )
        password_input.send_keys(password)

        # 4. Submit the form
        submit_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(submit_button_locator)
        )
        submit_button.click()

        # 5. Verify registration success
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(welcome_message_locator)
            )
            welcome_message_text = welcome_message.get_attribute("data-value")
            if welcome_message_text != "user":
                self.fail(f"Welcome message text is incorrect: {welcome_message_text}")
        except Exception as e:
            self.fail(f"Welcome message not found or incorrect: {e}")


if __name__ == "__main__":
    unittest.main()