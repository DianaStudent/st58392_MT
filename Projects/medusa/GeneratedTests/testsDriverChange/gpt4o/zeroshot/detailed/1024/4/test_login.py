import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Setup the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
    
    def test_login(self):
        driver = self.driver
        
        # Step 1: Open the home page is implicit with setUp
        
        # Step 2: Click the "Account" button
        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]'))
        )
        account_button.click()

        # Step 3: Wait for the login page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="login-page"]'))
        )

        # Step 4: Enter the email and password using credentials
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]'))
        )
        password_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="password-input"]')
        
        if not email_input or not password_input:
            self.fail("Email input or password input field is missing.")

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")
        
        # Step 5: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="sign-in-button"]')
        if not sign_in_button:
            self.fail("Sign in button is missing.")
        
        sign_in_button.click()

        # Step 6: Verify that the welcome message "Hello user" is present
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]'))
        )

        if not welcome_message or not welcome_message.text.strip():
            self.fail("Welcome message is missing or empty.")
        
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()