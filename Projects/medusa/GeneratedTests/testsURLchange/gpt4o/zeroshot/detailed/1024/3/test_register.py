import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def generate_unique_email(self):
        return f"user_{random.randint(1000, 9999)}@test.com"
    
    def test_user_registration(self):        
        driver = self.driver
        
        # Open the homepage
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        
        # Click the "Account" button
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]'))
        )
        account_button.click()
        
        # Click the "Join Us" button
        join_us_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]'))
        )
        join_us_button.click()
        
        # Fill the registration form
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form')))

        first_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="first-name-input"]')
        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        unique_email = self.generate_unique_email()
        email_input.send_keys(unique_email)
        password_input.send_keys("testuser")
        
        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        register_button.click()
        
        # Verify successful registration by checking the presence of welcome message
        try:
            welcome_message = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'))
            )
            self.assertIsNotNone(welcome_message)
            self.assertTrue("Hello user" in welcome_message.text)
        except Exception as e:
            self.fail(f"Registration not successful: {str(e)}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()