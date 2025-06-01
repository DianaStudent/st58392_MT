import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_button.click()

        # Step 3: Click the "Join Us" button
        join_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]')))
        join_button.click()

        # Step 4: Fill in all fields
        # First name
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]')))
        first_name_input.send_keys("user")

        # Last name
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')))
        last_name_input.send_keys("test")

        # Email - generating unique email
        unique_email = f'user_{int(time.time())}@test.com'
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="email-input"]')))
        email_input.send_keys(unique_email)

        # Password
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="password-input"]')))
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]')))
        register_button.click()

        # Step 6: Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        self.assertTrue(welcome_message and "Hello user" in welcome_message.text, "Registration failed - Welcome message not found")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()