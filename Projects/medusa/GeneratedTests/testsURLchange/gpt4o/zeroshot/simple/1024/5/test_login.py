import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MedusaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Or any other driver you're using
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Navigate to login page by clicking the Account link
        try:
            account_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click Account link: {e}")

        # Wait for the login page to load
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']")))
        except Exception as e:
            self.fail(f"Login page did not load: {e}")

        # Enter email
        try:
            email_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            email_input.send_keys("user@test.com")
        except Exception as e:
            self.fail(f"Failed to find or input email: {e}")

        # Enter password
        try:
            password_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='password-input']")))
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to find or input password: {e}")

        # Click sign in button
        try:
            sign_in_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']")))
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click sign in button: {e}")

        # Verify login success by checking for the welcome message
        try:
            welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail(f"Login did not succeed or welcome message not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()