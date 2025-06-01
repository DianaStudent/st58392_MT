import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def generate_unique_email(self):
        return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"

    def test_register_user(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click the "Account" link
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_link.click()

        # Click the "Join us" button
        join_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        join_button.click()

        # Fill in the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        unique_email = self.generate_unique_email()
        email_input.send_keys(unique_email)
        password_input.send_keys("testuser")

        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        register_button.click()

        # Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        self.assertIsNotNone(welcome_message, "Registration failed: Welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()