import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class MedusaRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_register_user(self):
        driver = self.driver

        # Navigate to account page
        account_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_link.click()

        # Click on 'Join us' to go to registration page
        join_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        join_button.click()

        # Fill out registration form
        first_name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        last_name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='last-name-input']")))
        email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']")))
        password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']")))

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        # Generate a unique email
        email_input.send_keys(f"user_{int(time.time())}@test.com")
        password_input.send_keys("testuser")

        # Submit the registration
        register_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        register_button.click()

        # Check for the welcome message to confirm registration success
        welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        
        # Assert that the welcome message contains correct username information
        welcome_text = welcome_message.get_attribute("data-value")
        self.assertEqual(welcome_text, "user", "Registration failed or Welcome message not found.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()