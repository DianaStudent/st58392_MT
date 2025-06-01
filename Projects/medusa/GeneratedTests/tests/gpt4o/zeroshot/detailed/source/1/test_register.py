import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)
    
    def generate_email(self):
        # Generate a unique email using timestamp and a random number
        return f"user_{int(time.time())}_{random.randint(1000, 9999)}@test.com"

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage (done in setUp)
        
        # Step 2: Click the "Account" button
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
        )
        account_button.click()
        
        # Step 3: Click the "Join Us" button below the login form
        join_us_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']"))
        )
        join_us_button.click()

        # Step 4: Fill in all fields: First name, Last name, and Password from credentials, generate unique email
        first_name_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']"))
        )
        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(self.generate_email())
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        submit_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        submit_button.click()

        # Step 6: Verify registration success by checking presence of welcome message "Hello user"
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message'][data-value='user']"))
        )
        
        if not welcome_message or welcome_message.text.strip() == "":
            self.fail("Welcome message not found or empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()