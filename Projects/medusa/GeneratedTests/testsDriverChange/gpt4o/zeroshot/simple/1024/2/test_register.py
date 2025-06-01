import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class MedusaStoreRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_user_registration(self):
        driver = self.driver
        
        # Navigate to account page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except:
            self.fail("Account link not found or not clickable.")
        
        # Click register button
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_button.click()
        except:
            self.fail("Register button not found or not clickable.")
        
        # Fill registration form
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
            )
            last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
            email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")

            # Generate a dynamic email address
            dynamic_email = f"user_{random.randint(1000, 9999)}@test.com"

            first_name_input.send_keys("user")
            last_name_input.send_keys("test")
            email_input.send_keys(dynamic_email)
            password_input.send_keys("testuser")
        except:
            self.fail("Failed to fill the registration form.")
        
        # Submit registration
        try:
            join_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
            join_button.click()
        except:
            self.fail("Join button not found or not clickable.")
        
        # Verify registration success
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text)
        except:
            self.fail("Registration success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()