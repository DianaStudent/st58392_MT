import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    URL = "http://localhost:8000/dk"
    CREDENTIALS = {"Email": "user@test.com", "Password": "testuser"}

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "Account" button in the right corner.
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        try:
            account_link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(account_link_locator)
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Account link not found or not clickable: {e}")

        # 3. Wait for the login page to load.
        email_input_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(email_input_locator)
            )
        except Exception as e:
            self.fail(f"Email input field not found on the login page: {e}")

        # 4. Enter the email and password using credentials.
        email_input = self.driver.find_element(*email_input_locator)
        password_input_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        password_input = self.driver.find_element(*password_input_locator)

        email_input.send_keys(self.CREDENTIALS["Email"])
        password_input.send_keys(self.CREDENTIALS["Password"])

        # 5. Click the sign-in button.
        sign_in_button_locator = (By.CSS_SELECTOR, '[data-testid="sign-in-button"]')
        try:
            sign_in_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(sign_in_button_locator)
            )
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Sign-in button not found or not clickable: {e}")

        # 6. Verify that the welcome message "Hello user" is present.
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        try:
            welcome_message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(welcome_message_locator)
            )
            self.assertEqual(welcome_message.text, "Hello user", "Welcome message is incorrect")
        except Exception as e:
            self.fail(f"Welcome message not found or incorrect: {e}")

if __name__ == "__main__":
    unittest.main()