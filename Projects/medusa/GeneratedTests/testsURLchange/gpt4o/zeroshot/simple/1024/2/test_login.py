import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Navigate to the login page
        try:
            account_link = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to find account link: {str(e)}")

        # Enter email
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")
        except Exception as e:
            self.fail(f"Failed to enter email: {str(e)}")

        # Enter password
        try:
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to enter password: {str(e)}")

        # Click sign-in button
        try:
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to click sign-in button: {str(e)}")

        # Confirm successful login by checking for welcome message
        try:
            welcome_message = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail(f"Failed to find welcome message: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()