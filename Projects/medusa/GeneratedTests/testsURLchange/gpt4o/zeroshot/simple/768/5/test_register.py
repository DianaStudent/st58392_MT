import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")

    def generate_random_email(self):
        return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"

    def test_user_registration(self):
        driver = self.driver

        # Navigate to Account page
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]'))
        )
        account_link.click()

        # Navigate to Registration page
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]'))
        )
        register_button.click()

        # Fill Registration form
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]'))
        )
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        email = self.generate_random_email()
        email_input.send_keys(email)

        phone_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="phone-input"]')
        phone_input.send_keys("1234567890")

        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
        password_input.send_keys("testuser")

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        submit_button.click()

        # Confirm registration success
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'))
        )
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()