import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserRegistrationTest(unittest.TestCase):
    URL = "http://localhost:8000/dk"
    FIRST_NAME = "user"
    LAST_NAME = "test"
    PASSWORD = "testuser"

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.URL)

        # 1. Click the "Account" button
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_link.click()

        # 2. Click the "Join us" button
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        register_button.click()

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

        email = f"user_{uuid.uuid4().hex}@test.com"
        first_name_input.send_keys(self.FIRST_NAME)
        last_name_input.send_keys(self.LAST_NAME)
        email_input.send_keys(email)
        password_input.send_keys(self.PASSWORD)

        # 4. Submit the form
        register_submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        register_submit_button.click()

        # 5. Verify registration success
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message and welcome_message.text:
            self.assertEqual("Hello user", welcome_message.text)
        else:
            self.fail("Welcome message is not present or empty")


if __name__ == "__main__":
    unittest.main()