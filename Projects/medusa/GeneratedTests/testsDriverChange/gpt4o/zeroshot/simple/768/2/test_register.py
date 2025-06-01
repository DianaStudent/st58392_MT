import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Account page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_link.click()

        # Switch to Register page
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        register_button.click()

        # Fill out the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")

        # Dynamically generate email
        email = "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@test.com"

        # Enter values
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(email)
        password_input.send_keys("testuser")

        # Submit the form
        join_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        join_button.click()

        # Verify successful registration
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        self.assertIn("Hello user", welcome_message.text, "Registration failed or welcome message is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()