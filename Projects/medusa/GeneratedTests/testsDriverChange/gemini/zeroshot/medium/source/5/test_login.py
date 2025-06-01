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
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_link.click()

        # 3. Wait for the login page to load.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']"))
        )

        # 4. Enter the email and password.
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # 5. Click the sign-in button.
        sign_in_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
        )
        sign_in_button.click()

        # 6. Verify that the welcome message is present.
        try:
            welcome_message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertTrue(welcome_message.is_displayed(), "Welcome message is not displayed.")
            self.assertIn("Hello user", welcome_message.text, "Incorrect welcome message.")
        except Exception as e:
            self.fail(f"Welcome message not found or incorrect: {e}")

if __name__ == "__main__":
    unittest.main()