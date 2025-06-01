import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage
        # Homepage is already opened in setUp()

        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]')))
        account_button.click()

        # Step 3: Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="register-button"]')))
        join_us_button.click()

        # Step 4: Fill in all fields
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="first-name-input"]')))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="last-name-input"]')))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]')))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]')))

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        
        unique_email = f"user_{random.randint(1000, 9999)}@test.com"
        email_input.send_keys(unique_email)
        
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="register-button"]')
        register_button.click()

        # Step 6: Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]')))
        if not welcome_message or not welcome_message.text.strip():
            self.fail("Welcome message is missing or empty")
        
        self.assertIn("Hello user", welcome_message.text)

if __name__ == "__main__":
    unittest.main()