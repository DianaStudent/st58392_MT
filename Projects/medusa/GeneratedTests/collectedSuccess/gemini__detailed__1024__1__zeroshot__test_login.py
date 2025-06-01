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
        self.url = "http://localhost:8000/dk"
        self.email = "user@test.com"
        self.password = "testuser"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Open the home page.
        # 2. Click the "Account" button in the right corner.
        account_link_locator = (By.CSS_SELECTOR, "a[data-testid='nav-account-link']")
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(account_link_locator)
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Account link not found or not clickable: {e}")

        # 3. Wait for the login page to load.
        email_input_locator = (By.CSS_SELECTOR, "input[data-testid='email-input']")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(email_input_locator)
            )
        except Exception as e:
            self.fail(f"Email input field not found: {e}")

        # 4. Enter the email and password using credentials.
        email_input = driver.find_element(*email_input_locator)
        email_input.send_keys(self.email)

        password_input_locator = (By.CSS_SELECTOR, "input[data-testid='password-input']")
        password_input = driver.find_element(*password_input_locator)
        password_input.send_keys(self.password)

        # 5. Click the sign-in button.
        sign_in_button_locator = (By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(sign_in_button_locator)
            )
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Sign-in button not found or not clickable: {e}")

        # 6. Verify that the welcome message "Hello user" is present.
        welcome_message_locator = (By.CSS_SELECTOR, "span[data-testid='welcome-message']")
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(welcome_message_locator)
            )
            welcome_message_text = welcome_message.text
            self.assertEqual(welcome_message_text, "Hello user", "Welcome message is incorrect")
        except Exception as e:
            self.fail(f"Welcome message not found or incorrect: {e}")

if __name__ == "__main__":
    unittest.main()