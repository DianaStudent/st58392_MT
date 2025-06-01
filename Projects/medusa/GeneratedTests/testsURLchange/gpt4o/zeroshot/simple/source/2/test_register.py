import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to Account page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Go to Register page
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        register_button.click()

        # Fill the registration form
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))).send_keys("user")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))).send_keys("test")
        email = f"user_{int(time.time())}@test.com"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='phone-input']"))).send_keys("5551234567")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))).send_keys("testuser")

        # Submit the registration form
        register_submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        register_submit_button.click()

        # Confirm registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        self.assertIsNotNone(welcome_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()