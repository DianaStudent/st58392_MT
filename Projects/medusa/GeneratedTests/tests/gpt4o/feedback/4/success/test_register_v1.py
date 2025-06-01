from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage and click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_button.click()

        # Step 2: Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        join_us_button.click()

        # Step 3: Fill in registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='last-name-input']")))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']")))
        
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        
        # Generate a unique email
        unique_email = f"user_{random.randint(1000, 9999)}@test.com"
        email_input.send_keys(unique_email)

        password_input.send_keys("testuser")

        # Step 4: Submit the registration form
        submit_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button'][type='submit']")
        submit_button.click()

        # Step 5: Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))

        if not welcome_message or not welcome_message.text.startswith("Hello user"):
            self.fail("Registration success message not found or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()