import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        
        # Navigate to the account page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
            )
            account_link.click()
        except:
            self.fail("Account link not found")

        # Click on the register button
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']"))
            )
            register_button.click()
        except:
            self.fail("Register button not found")

        # Fill out the registration form
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-page']"))
            )

            first_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='first-name-input']")
            last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
            email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
            password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")

            first_name_input.send_keys("user")
            last_name_input.send_keys("test")

            # Generate a unique email
            unique_email = f"user_{random.randint(10000, 99999)}@test.com"
            email_input.send_keys(unique_email)

            password_input.send_keys("testuser")

            # Submit the registration form
            join_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
            join_button.click()

        except:
            self.fail("Registration form not filled out correctly")

        # Confirm registration success
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text, "Welcome message is missing or incorrect")
        except:
            self.fail("Registration confirmation failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()