import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the home page (already done in setUp)
        
        # 2. Click the "Account" button
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if account_button is None or not account_button.is_displayed():
            self.fail("Account button is not present or not visible.")
        account_button.click()
        
        # 3. Wait for the login page to load
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']"))
        )
        
        # 4. Enter the email and password
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        
        if email_input is None or password_input is None:
            self.fail("Email or Password input field is not present.")
        
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")
        
        # 5. Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        if sign_in_button is None:
            self.fail("Sign in button is not present.")
        sign_in_button.click()
        
        # 6. Verify that the welcome message "Hello user" is present
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )
        
        if welcome_message is None or not welcome_message.text:
            self.fail("Welcome message is not present or empty.")
        
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()