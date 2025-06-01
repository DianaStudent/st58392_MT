import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        """Generate a random email address."""
        return ''.join(random.choice(string.ascii_letters) for _ in range(10)) + "@test.com"

    def test_registration_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Account Page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_link.click()

        # Navigate to Registration Form
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        register_button.click()

        # Fill Registration Form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        phone_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='phone-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(self.generate_email())
        phone_input.send_keys("0000000000")
        password_input.send_keys("testuser")

        # Submit Registration
        join_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        join_button.click()

        # Validate Registration Success
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail("Registration was not successful: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()