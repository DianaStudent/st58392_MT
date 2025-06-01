from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class MedusaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver

        # 1. Open the home page and verify the page loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
        )
        
        # 2. Click the "Account" button
        account_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='nav-account-link']")
        account_button.click()

        # 3. Wait for the login page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page']"))
        )

        # 4. Enter the email and password using credentials
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # 5. Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='sign-in-button']")
        sign_in_button.click()

        # 6. Verify that the welcome message "Hello user" is present
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
        )

        # Check if the welcome message contains the expected text
        if not welcome_message or "Hello user" not in welcome_message.text:
            self.fail("Welcome message 'Hello user' not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()