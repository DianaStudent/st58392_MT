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

        # Step 2: Click the "Account" link.
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        if not account_link:
            self.fail("Account link is missing or not loaded on the page.")
        account_link.click()

        # Step 3: Wait for the login page to load.
        login_page_header = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page'] h1")))
        if not login_page_header or login_page_header.text.strip() == "":
            self.fail("Login page header is missing or empty.")
        
        # Step 4: Enter the email and password.
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))
        
        if not email_input:
            self.fail("Email input is missing or not loaded on the page.")
        
        if not password_input:
            self.fail("Password input is missing or not loaded on the page.")
        
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")
        
        # Step 5: Click the sign-in button.
        sign_in_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='sign-in-button']")))
        if not sign_in_button:
            self.fail("Sign-in button is missing or not loaded on the page.")
        sign_in_button.click()

        # Step 6: Verify that the welcome message is present.
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        if not welcome_message or welcome_message.text.strip() == "":
            self.fail("Welcome message is missing or empty, login might have failed.")
        
        # Confirming success by checking welcome message text
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()