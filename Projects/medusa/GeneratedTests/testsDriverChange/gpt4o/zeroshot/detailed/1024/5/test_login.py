import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_button.click()

        # Step 3: Wait for the login page to load
        login_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page']")))

        # Step 4: Enter the email and password
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        
        if not email_input or not password_input:
            self.fail("Email or Password input field is missing")
        
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='sign-in-button']")
        sign_in_button.click()

        # Step 6: Verify that the welcome message "Hello user" is present
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail(f"Login failed or welcome message missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()