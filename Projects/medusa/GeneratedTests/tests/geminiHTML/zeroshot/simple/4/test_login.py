import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Navigate to the account page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click account link: {e}")

        # Find and fill in the email field
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")
        except Exception as e:
            self.fail(f"Failed to find or fill email input: {e}")

        # Find and fill in the password field
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to find or fill password input: {e}")

        # Click the sign-in button
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
            )
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click sign-in button: {e}")

        # Verify successful login by checking for the welcome message
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertEqual(welcome_message.get_attribute("data-value"), "user", "Login failed: Welcome message incorrect")
        except Exception as e:
            self.fail(f"Login failed: Welcome message not found or incorrect: {e}")

if __name__ == "__main__":
    unittest.main()