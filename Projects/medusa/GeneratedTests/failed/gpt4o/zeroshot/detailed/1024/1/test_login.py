from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page (already done in setup)

        # Step 2: Click the "Account" button in the right left corner.
        account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_button.click()

        # Step 3: Wait for the login page to load.
        email_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )

        # Step 4: Enter the email and password using credentials.
        if not email_input:
            self.fail("Email input field not available")

        password_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )
        if not password_input:
            self.fail("Password input field not available")

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button.
        sign_in_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
        )
        if not sign_in_button:
            self.fail("Sign-in button not available")

        sign_in_button.click()

        # Step 6: Verify that the welcome message "Hello user" is present.
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='mobile-account-nav'] div"))
        )
        
        if not welcome_message or "Hello user" not in welcome_message.text:
            self.fail("Welcome message 'Hello user' was not found")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()