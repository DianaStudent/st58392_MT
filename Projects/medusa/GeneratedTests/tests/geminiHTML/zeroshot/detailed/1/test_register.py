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
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the "Account" button in the right corner.
        account_link_locator = (By.CSS_SELECTOR, "a[data-testid='nav-account-link']")
        account_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located(account_link_locator))

        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 3. Click the "Join us" button below the login form.
        register_button_locator = (By.CSS_SELECTOR, "button[data-testid='register-button']")
        register_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(register_button_locator))

        if register_button:
            register_button.click()
        else:
            self.fail("Register button not found")

        # 4. Fill in all fields: first name, last name, email, and password.
        first_name_input_locator = (By.CSS_SELECTOR, "input[data-testid='first-name-input']")
        last_name_input_locator = (By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        email_input_locator = (By.CSS_SELECTOR, "input[data-testid='email-input']")
        password_input_locator = (By.CSS_SELECTOR, "input[data-testid='password-input']")

        first_name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(first_name_input_locator))
        last_name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(last_name_input_locator))
        email_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(email_input_locator))
        password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(password_input_locator))

        if not all([first_name_input, last_name_input, email_input, password_input]):
            self.fail("One or more input fields not found")

        first_name = "user"
        last_name = "test"
        email = f"user_{uuid.uuid4().hex}@test.com"
        password = "testuser"

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        password_input.send_keys(password)

        # 5. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, "button[data-testid='register-button']")
        submit_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(submit_button_locator))

        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 6. Verify registration success by checking presence of welcome message "Hello user".
        welcome_message_locator = (By.CSS_SELECTOR, "span[data-testid='welcome-message']")
        welcome_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located(welcome_message_locator))

        if welcome_message:
            actual_message = welcome_message.text
            self.assertEqual(actual_message, "Hello user", "Registration failed. Welcome message not found or incorrect.")
        else:
            self.fail("Welcome message not found after registration.")

if __name__ == "__main__":
    unittest.main()