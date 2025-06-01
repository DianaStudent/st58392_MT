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
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open home page (done in setUp)
        
        # Step 2: Click the "Account" button
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_link.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="login-page"]')))
        
        # Step 4: Enter the email and password
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')

        if not email_input or not password_input:
            self.fail("Email or Password input field is missing.")
        
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")
        
        # Step 5: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')
        
        if not sign_in_button:
            self.fail("Sign in button is missing.")
        
        sign_in_button.click()
        
        # Step 6: Verify that the welcome message "Hello user" is present
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        
        if not welcome_message:
            self.fail("Welcome message is missing.")
        
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()