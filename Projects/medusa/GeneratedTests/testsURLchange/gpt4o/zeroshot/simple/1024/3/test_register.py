import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to account page
        account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Click on register button
        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        register_button.click()

        # Fill in registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        
        # Generate a random email
        random_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(random_email)
        
        password_input.send_keys("testuser")

        # Click the join button
        join_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        join_button.click()

        # Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        
        if not welcome_message.is_displayed():
            self.fail("Registration failed, welcome message not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()