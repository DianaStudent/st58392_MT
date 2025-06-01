from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the home page.
        # Wait until the "Account" button is present and click it
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_button.click()

        # 3. Wait for the login page to load.
        # Ensure login page loads by checking for the email input field
        email_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")

        # Ensure the inputs are visible
        if not email_input.is_displayed() or not password_input.is_displayed():
            self.fail("Email or Password input is not displayed.")

        # 4. Enter the email and password using credentials.
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # 5. Click the sign-in button.
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        sign_in_button.click()

        # 6. Verify that the welcome message "Hello user" is present.
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )
        
        # Check if the welcome message is not empty
        if not welcome_message.text.strip():
            self.fail("Welcome message is empty.")
        
        self.assertIn("Hello user", welcome_message.text, "Welcome message does not contain 'Hello user'.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()