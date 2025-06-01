import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        if not account_button or account_button.text.strip() == '':
            self.fail("Account button is not present or empty.")
        
        account_button.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']")))

        # Step 4: Enter email and password
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
        if not email_input:
            self.fail("Email input is not present.")

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))
        if not password_input:
            self.fail("Password input is not present.")
        
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='sign-in-button']")))
        if not sign_in_button or sign_in_button.text.strip() == '':
            self.fail("Sign-in button is not present or empty.")
        
        sign_in_button.click()

        # Step 6: Verify that the welcome message "Hello user" is present
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        if not welcome_message or welcome_message.text.strip() == '':
            self.fail("Welcome message is not present or empty.")
        
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()