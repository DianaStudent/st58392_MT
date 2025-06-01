import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Go to the account page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Go to the registration page
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        register_button.click()

        # Fill out the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(self.generate_random_email())
        password_input.send_keys("testuser")

        # Submit the form
        join_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        join_button.click()

        # Check for the welcome message
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except:
            self.fail("Welcome message not found. Registration may have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()