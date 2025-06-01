import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "Account" link.
        account_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 3. Wait for the login page to load.
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        if not email_input:
            self.fail("Email input field not found on login page")

        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )
        if not password_input:
            self.fail("Password input field not found on login page")

        # 4. Enter the email and password.
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # 5. Click the sign-in button.
        sign_in_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
        )
        if sign_in_button:
            sign_in_button.click()
        else:
            self.fail("Sign-in button not found")

        # 6. Verify that the welcome message is present.
        welcome_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message:
            welcome_message_text = welcome_message.get_attribute("data-value")
            if welcome_message_text and welcome_message_text.strip():
                self.assertEqual(welcome_message_text, "user", "Welcome message is incorrect")
            else:
                self.fail("Welcome message text is empty")
        else:
            self.fail("Welcome message not found after login")

if __name__ == "__main__":
    unittest.main()