import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class LoginTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Click the "Account" button in the right corner.
        try:
            account_link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to click account link: {e}")

        # 3. Wait for the login page to load.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']"))
            )
        except Exception as e:
            self.fail(f"Login page did not load: {e}")

        # 4. Enter the email and password using credentials.
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )

            email_input.send_keys("user@test.com")
            password_input.send_keys("testuser")

        except Exception as e:
            self.fail(f"Failed to enter credentials: {e}")

        # 5. Click the sign-in button.
        try:
            sign_in_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
            )
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to click sign-in button: {e}")

        # 6. Verify that the welcome message "Hello user" is present.
        try:
            welcome_message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message'][data-value='user']"))
            )
            self.assertEqual(welcome_message.text, "Hello user")
        except Exception as e:
            self.fail(f"Welcome message not found or incorrect: {e}")


if __name__ == "__main__":
    unittest.main()