import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class MedusaStoreRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage and click the "Account" button in the top right corner
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_button.click()

        # Step 2: Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        join_us_button.click()

        # Step 3: Fill in the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        last_name_input.send_keys("test")

        # Generate a unique email
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        unique_email = f"user_{random.randint(1000, 9999)}@test.com"
        email_input.send_keys(unique_email)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        password_input.send_keys("testuser")

        # Submit the form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        register_button.click()

        # Step 4: Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        if not welcome_message or "Hello user" not in welcome_message.text:
            self.fail("Registration failed - Welcome message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()