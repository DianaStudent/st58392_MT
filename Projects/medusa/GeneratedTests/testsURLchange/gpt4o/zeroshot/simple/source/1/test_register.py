import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the account page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_link.click()

        # Click on the register button on the login page
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]')))
        register_button.click()

        # Fill the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]')))
        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        phone_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="phone-input"]')
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')

        # Using time to generate a unique email
        unique_email = f"user_{int(time.time())}@test.com"

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(unique_email)
        phone_input.send_keys("1234567890")
        password_input.send_keys("testuser")

        # Submit the registration form
        join_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        join_button.click()

        # Verify registration by checking the welcome message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        
        if welcome_message.get_attribute('data-value') != 'user':
            self.fail("Registration failed, welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()