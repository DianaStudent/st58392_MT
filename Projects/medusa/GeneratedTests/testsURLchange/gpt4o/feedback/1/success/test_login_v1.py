import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        try:
            # Step 2: Click the "Account" button
            account_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_button.click()

            # Step 3: Wait for the login page to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']"))
            )

            # Step 4: Enter the email
            email_input = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
            if not email_input:
                self.fail("Email input not found")
            email_input.send_keys("user@test.com")

            # Enter the password
            password_input = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            if not password_input:
                self.fail("Password input not found")
            password_input.send_keys("testuser")

            # Step 5: Click the sign-in button
            sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            if not sign_in_button:
                self.fail("Sign-in button not found")
            sign_in_button.click()

            # Step 6: Verify the welcome message
            welcome_message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            if not welcome_message:
                self.fail("Welcome message not found")
            self.assertIn("Hello user", welcome_message.text)

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()