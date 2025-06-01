import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Navigate to Account page
        try:
            account_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()
        except TimeoutException:
            self.fail("Failed to find the account link on the home page")

        # Enter Email
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            email_input.send_keys("user@test.com")
        except TimeoutException:
            self.fail("Failed to find the email input field on the login page")

        # Enter Password
        try:
            password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))
            password_input.send_keys("testuser")
        except TimeoutException:
            self.fail("Failed to find the password input field on the login page")

        # Click Sign In
        try:
            sign_in_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']")))
            sign_in_button.click()
        except TimeoutException:
            self.fail("Failed to find or click the sign-in button on the login page")

        # Confirm success by checking the welcome message
        try:
            welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message'][data-value='user']")))
            self.assertTrue(welcome_message.is_displayed(), "Login failed or welcome message is not displayed")
        except TimeoutException:
            self.fail("Failed to find the welcome message after login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()