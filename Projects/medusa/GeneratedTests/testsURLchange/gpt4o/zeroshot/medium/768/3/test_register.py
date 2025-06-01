import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def generate_email(self):
        return f"user_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@test.com"

    def test_registration(self):
        driver = self.driver

        # Step 2: Click the "Account" link
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]'))
        )
        account_link.click()

        # Step 3: Click the "Join Us" button
        join_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]'))
        )
        join_button.click()

        # Step 4: Fill in all fields: first name, last name, email, password
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]'))
        )
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        last_name_input.send_keys("test")

        email = self.generate_email()
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        email_input.send_keys(email)

        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        register_button.click()

        # Step 6: Verify registration success by checking presence of welcome message
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'))
        )
        
        self.assertTrue(welcome_message and welcome_message.text.strip(), "Welcome message not found or empty.")

if __name__ == "__main__":
    unittest.main()