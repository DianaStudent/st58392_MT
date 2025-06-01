import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestMedusaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver

        # Step 1: Click the "Account" button
        account_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_button.click()

        # Step 2: Wait for the login page to load
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="login-page"]')))
        
        # Step 3: Enter the email and password
        email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="email-input"]')))
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
        
        email_input.send_keys('user@test.com')
        password_input.send_keys('testuser')

        # Step 4: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')
        sign_in_button.click()

        # Step 5: Verify the welcome message
        welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        self.assertEqual(welcome_message.text, "Hello user", "Login failed or welcome message is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()