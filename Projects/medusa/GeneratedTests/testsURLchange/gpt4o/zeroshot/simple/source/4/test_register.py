import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_register_user(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to account page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_link.click()

        # Click on register button
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]')))
        register_button.click()

        # Fill registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]')))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        unique_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(unique_email)

        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
        password_input.send_keys("testuser")

        register_submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        register_submit_button.click()

        # Confirm registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))

        if not welcome_message:
            self.fail("Registration failed - welcome message not found.")
        
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()