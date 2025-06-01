import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def generate_email(self):
        # Generates a unique email each time by appending a timestamp
        timestamp = int(time.time())
        return f"user_{timestamp}@test.com"

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" link.
        account_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_link.click()

        # Step 3: Click the "Join Us" button.
        join_us_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        join_us_button.click()

        # Step 4: Fill in all fields for registration.
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))).send_keys("user")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))).send_keys("test")
        email = self.generate_email()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))).send_keys("testuser")
        
        # Step 5: Submit the registration form.
        register_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        register_button.click()

        # Step 6: Verify registration success by checking the presence of the welcome message.
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )
        if not welcome_message or not welcome_message.text:
            self.fail("Registration failed or the welcome message is not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()