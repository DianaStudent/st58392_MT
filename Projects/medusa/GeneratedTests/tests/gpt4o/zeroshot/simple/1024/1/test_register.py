import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
import string

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8000/dk")

    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"user_{random_string}@test.com"

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Account Page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]')))
        account_link.click()

        # Go to Registration Page
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="register-button"]')))
        register_button.click()

        # Fill Registration Form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="first-name-input"]')))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="email-input"]')
        email = self.generate_random_email()
        email_input.send_keys(email)

        password_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="password-input"]')
        password_input.send_keys("testuser")

        # Submit the Form
        join_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="register-button"]')
        join_button.click()

        # Confirm Successful Registration
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]')))
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()