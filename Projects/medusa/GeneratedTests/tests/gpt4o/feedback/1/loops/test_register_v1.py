import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get('http://localhost:8000/dk')
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to account page
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
        )
        account_button.click()

        # Navigate to registration page
        join_us_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']"))
        )
        join_us_button.click()

        # Fill registration form
        first_name_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']"))
        )
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        generated_email = f"user_{random.randint(1000, 9999)}@test.com"
        email_input.send_keys(generated_email)

        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        password_input.send_keys("testuser")

        # Submit the form
        register_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        register_button.click()

        # Verify registration success
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
        )
        self.assertTrue(welcome_message.is_displayed() and welcome_message.text == "Hello user")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()