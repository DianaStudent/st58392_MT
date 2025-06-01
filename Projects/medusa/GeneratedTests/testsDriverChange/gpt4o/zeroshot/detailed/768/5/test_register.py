import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_user_registration(self):
        driver = self.driver
        
        # Step 2: Click the "Account" button
        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]'))
        )
        account_button.click()

        # Step 3: Click the "Join Us" button
        join_us_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="register-button"]'))
        )
        join_us_button.click()

        # Step 4: Fill in all fields: first name, last name, email, and password
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="first-name-input"]'))
        )
        last_name_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        email_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="email-input"]')
        password_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="password-input"]')
        
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        
        # Generating a unique email
        unique_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(unique_email)
        
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_button.click()

        # Step 6: Verify registration success
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]'))
        )

        if not welcome_message or not welcome_message.text:
            self.fail("Registration failed: Welcome message not found or empty.")

        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()