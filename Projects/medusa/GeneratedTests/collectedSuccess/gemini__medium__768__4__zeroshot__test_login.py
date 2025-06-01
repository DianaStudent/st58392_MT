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
        driver = self.driver
        email = "user@test.com"
        password = "testuser"

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "Account" link.
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to click account link: {e}")

        # 3. Wait for the login page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']"))
            )
        except Exception as e:
            self.fail(f"Login page did not load: {e}")

        # 4. Enter the email and password.
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )
            email_input.send_keys(email)
            password_input.send_keys(password)
        except Exception as e:
            self.fail(f"Failed to enter credentials: {e}")

        # 5. Click the sign-in button.
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
            )
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to click sign-in button: {e}")

        # 6. Verify that the welcome message is present.
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIsNotNone(welcome_message.text)
            self.assertNotEqual(welcome_message.text, "")
        except Exception as e:
            self.fail(f"Welcome message not found: {e}")

if __name__ == "__main__":
    unittest.main()