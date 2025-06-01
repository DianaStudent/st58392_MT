import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        
        # Navigate to account page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click on the account link: {e}")

        # Enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")
        except Exception as e:
            self.fail(f"Failed to find or interact with the email input: {e}")

        # Enter password
        try:
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to find or interact with the password input: {e}")

        # Click sign in
        try:
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click on the sign in button: {e}")

        # Verify login success
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail(f"Login was unsuccessful or welcome message not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()