import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Open the homepage. (Already done in setUp)

        # 2. Click the "Account" button in the right corner.
        account_link_locator = (By.CSS_SELECTOR, "a[data-testid='nav-account-link']")
        account_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located(account_link_locator))
        account_link.click()

        # 3. Click the "Join us" button below the login form.
        register_button_locator = (By.CSS_SELECTOR, "button[data-testid='register-button']")
        register_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(register_button_locator))
        register_button.click()

        # 4. Fill in all fields: first name, last name, email, and password.
        first_name_input_locator = (By.CSS_SELECTOR, "input[data-testid='first-name-input']")
        first_name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(first_name_input_locator))
        first_name_input.send_keys("user")

        last_name_input_locator = (By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        last_name_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(last_name_input_locator))
        last_name_input.send_keys("test")

        email = f"user_{uuid.uuid4().hex}@test.com"
        email_input_locator = (By.CSS_SELECTOR, "input[data-testid='email-input']")
        email_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(email_input_locator))
        email_input.send_keys(email)

        phone_input_locator = (By.CSS_SELECTOR, "input[data-testid='phone-input']")
        phone_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(phone_input_locator))
        phone_input.send_keys("1234567890")

        password_input_locator = (By.CSS_SELECTOR, "input[data-testid='password-input']")
        password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located(password_input_locator))
        password_input.send_keys("testuser")

        # 5. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, "button[data-testid='register-button']")
        submit_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(submit_button_locator))
        submit_button.click()

        # 6. Verify registration success by checking presence of welcome message "Hello user".
        welcome_message_locator = (By.CSS_SELECTOR, "span[data-testid='welcome-message']")
        try:
            welcome_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located(welcome_message_locator))
            welcome_text = welcome_message.text
            self.assertEqual(welcome_text, "Hello user", "Registration failed: Welcome message not found or incorrect.")
        except Exception as e:
            self.fail(f"Registration failed: Welcome message not found after registration. Error: {e}")

if __name__ == "__main__":
    unittest.main()