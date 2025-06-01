import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login_process(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        
        if not account_button or account_button.text.strip() == "":
            self.fail("Account button is missing or empty.")
        
        account_button.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page']")))

        # Step 4: Enter the email and password
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']")))

        if not email_input or not password_input:
            self.fail("Email or password input fields are missing.")

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='sign-in-button']")))
        
        if not sign_in_button:
            self.fail("Sign-in button is missing.")
            
        sign_in_button.click()

        # Step 6: Verify the welcome message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))

        if not welcome_message or welcome_message.text.strip() != "Hello user":
            self.fail("Welcome message is incorrect or missing.")
        

if __name__ == "__main__":
    unittest.main()