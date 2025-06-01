import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8000/dk')

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Step 1: Open the home page (already done in setUp).

        # Step 2: Click the "Account" button in the right-left corner.
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]'))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Failed to locate or click the Account button: {str(e)}")

        # Step 3: Wait for the login page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="login-page"]'))
            )
        except Exception as e:
            self.fail(f"Login page did not load: {str(e)}")

        # Step 4: Enter the email and password using credentials.
        try:
            email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
            password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
            
            email_input.send_keys("user@test.com")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to enter credentials: {str(e)}")

        # Step 5: Click the sign-in button.
        try:
            sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to click Sign-in button: {str(e)}")

        # Step 6: Verify that the welcome message "Hello user" is present.
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'))
            )
            
            self.assertIsNotNone(welcome_message)
            self.assertIn("Hello user", welcome_message.text)
        
        except Exception as e:
            self.fail(f"Failed to verify welcome message: {str(e)}")

if __name__ == '__main__':
    unittest.main()