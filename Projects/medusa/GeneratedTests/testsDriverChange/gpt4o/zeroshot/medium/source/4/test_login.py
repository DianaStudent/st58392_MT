from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class MedusaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Step 2: Click the "Account" link
        account_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        if not account_link:
            self.fail("Account link not found or not clickable.")
        account_link.click()

        # Step 3: Wait for the login page to load
        login_page = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="login-page"]')))
        if not login_page:
            self.fail("Login page did not load.")

        # Step 4: Enter the email and password
        email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="email-input"]')))
        password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="password-input"]')))
        if not email_input or not password_input:
            self.fail("Email or password input not found.")

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')))
        if not sign_in_button:
            self.fail("Sign-in button not found or not clickable.")
        sign_in_button.click()

        # Step 6: Verify that the welcome message is present
        welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        if not welcome_message or not welcome_message.text.strip():
            self.fail("Welcome message not found or is empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()