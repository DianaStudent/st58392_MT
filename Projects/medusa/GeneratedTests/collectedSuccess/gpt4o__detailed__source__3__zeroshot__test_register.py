import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        self.assertIsNotNone(account_button, "Account button not found.")
        account_button.click()

        # Step 2: Click the "Join us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        self.assertIsNotNone(join_us_button, "Join us button not found.")
        join_us_button.click()

        # Step 3: Fill the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        self.assertIsNotNone(first_name_input, "First name input not found.")
        first_name_input.send_keys("user")
        
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        self.assertIsNotNone(last_name_input, "Last name input not found.")
        last_name_input.send_keys("test")
        
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        self.assertIsNotNone(email_input, "Email input not found.")
        email_input.send_keys(f"user_{int(time.time())}@test.com")
        
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        self.assertIsNotNone(password_input, "Password input not found.")
        password_input.send_keys("testuser")

        # Step 4: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        self.assertIsNotNone(register_button, "Register button not found.")
        register_button.click()

        # Step 5: Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        self.assertIsNotNone(welcome_message, "Welcome message not found.")
        self.assertEqual(welcome_message.text, "Hello user")

if __name__ == '__main__':
    unittest.main()