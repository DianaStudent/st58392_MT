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

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage.
        # 2. Click the "Account" link.
        account_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 3. Click the "Join us" button.
        register_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if register_button:
            register_button.click()
        else:
            self.fail("Join us button not found")

        # 4. Fill in all fields: first name, last name, email (generate it unique), password.
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
        )
        last_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
        )
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )

        if not all([first_name_input, last_name_input, email_input, password_input]):
            self.fail("One or more input fields not found")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email = f"user_{uuid.uuid4().hex[:6]}@test.com"
        email_input.send_keys(email)
        password_input.send_keys("testuser")

        # 5. Submit the registration form.
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Register button not found")

        # 6. Verify registration success by checking presence of welcome message.
        welcome_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message and welcome_message.text:
            self.assertTrue("Hello user" in welcome_message.text)
        else:
            self.fail("Welcome message not found or is empty")


if __name__ == "__main__":
    unittest.main()