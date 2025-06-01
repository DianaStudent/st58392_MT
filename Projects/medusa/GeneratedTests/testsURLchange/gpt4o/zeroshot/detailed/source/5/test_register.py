from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import uuid

class TestMedusaRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage (Already done in setUp)
        
        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]')))
        account_button.click()

        # Step 3: Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="register-button"]')))
        join_us_button.click()

        # Step 4: Fill in the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="first-name-input"]')))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="last-name-input"]')))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]')))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]')))

        unique_email = f"user_{uuid.uuid4().hex[:8]}@test.com"

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(unique_email)
        password_input.send_keys("testuser")

        register_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="register-button"]')
        self.assertTrue(register_button.get_attribute('type') == 'submit')
        register_button.click()

        # Step 6: Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]')))
        self.assertTrue("Hello user" in welcome_message.text, "Registration failed: Welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()