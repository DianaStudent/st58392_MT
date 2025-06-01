from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver

        try:
            # Click the "Account" link
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
            )
            account_link.click()

            # Wait for the login page to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page']"))
            )

            # Enter the email
            email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
            if not email_input:
                self.fail("Email input is not present.")
            email_input.send_keys("user@test.com")

            # Enter the password
            password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
            if not password_input:
                self.fail("Password input is not present.")
            password_input.send_keys("testuser")

            # Click the sign-in button
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='sign-in-button']")
            if not sign_in_button:
                self.fail("Sign-in button is not present.")
            sign_in_button.click()

            # Verify the welcome message is present
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
            )
            if not welcome_message:
                self.fail("Welcome message is not present.")
            self.assertIn("Hello user", welcome_message.text)

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()