import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome options
        options = Options()
        options.add_argument("--headless")  # Run headless if needed
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage
        # Already done in setUp method

        # 2. Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]')))
        account_button.click()

        # 3. Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="register-button"]')))
        join_us_button.click()

        # 4. Fill in the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="first-name-input"]')))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="last-name-input"]')))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]')))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]')))
        
        # Fill out the form
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(f"user_{int(time.time())}@test.com")  # Generate unique email
        password_input.send_keys("testuser")

        # Submit the form
        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="register-button"]')))
        register_button.click()

        # 5. Verify registration success by checking "Hello user" message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]')))
        self.assertIsNotNone(welcome_message, "The welcome message was not found after registration.")
        self.assertTrue("Hello user" in welcome_message.text, "Registration did not succeed as expected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()