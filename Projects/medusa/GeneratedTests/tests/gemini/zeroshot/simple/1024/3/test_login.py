import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.email = "user@test.com"
        self.password = "testuser"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Navigate to account page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except:
            self.fail("Account link not found")

        # Find email input and enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys(self.email)
        except:
            self.fail("Email input not found")

        # Find password input and enter password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )
            password_input.send_keys(self.password)
        except:
            self.fail("Password input not found")

        # Find sign-in button and click
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
            )
            sign_in_button.click()
        except:
            self.fail("Sign-in button not found")

        # Verify successful login by checking for welcome message
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertEqual(welcome_message.get_attribute("data-value"), "user", "Login failed. Welcome message incorrect.")
        except:
            self.fail("Welcome message not found after login")

if __name__ == "__main__":
    unittest.main()