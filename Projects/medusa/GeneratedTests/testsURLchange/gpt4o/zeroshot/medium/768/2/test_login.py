import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MedusaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click the "Account" link
        account_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        if not account_link:
            self.fail("Account link not found on home page")
        account_link.click()

        # Step 2: Wait for the login page to load
        login_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']")))
        if not login_page:
            self.fail("Login page did not load")

        # Step 3: Enter the email and password
        email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
        if not email_input:
            self.fail("Email input field not found")

        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))
        if not password_input:
            self.fail("Password input field not found")
        
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 4: Click the sign-in button
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']")))
        if not sign_in_button:
            self.fail("Sign in button not found")
        sign_in_button.click()

        # Step 5: Verify that the welcome message is present
        welcome_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        if not welcome_message or not welcome_message.text:
            self.fail("Welcome message not found or empty after login")

        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()