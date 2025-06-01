import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestRegistrationProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def generate_unique_email(self):
        return f"user_{int(time.time())}@test.com"

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" button.
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        self.assertIsNotNone(account_button, "Account button is missing.")
        account_button.click()

        # Step 3: Click the "Join Us" button.
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        self.assertIsNotNone(join_us_button, "Join Us button is missing.")
        join_us_button.click()

        # Step 4: Fill in the registration form.
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='last-name-input']")))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']")))

        # Assert the fields are present
        self.assertIsNotNone(first_name_input, "First name input is missing.")
        self.assertIsNotNone(last_name_input, "Last name input is missing.")
        self.assertIsNotNone(email_input, "Email input is missing.")
        self.assertIsNotNone(password_input, "Password input is missing.")

        # Fill the form
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        unique_email = self.generate_unique_email()
        email_input.send_keys(unique_email)
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form.
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        self.assertIsNotNone(register_button, "Register button is missing.")
        register_button.click()

        # Step 6: Verify registration success.
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        self.assertIsNotNone(welcome_message, "Welcome message is missing.")
        self.assertEqual(welcome_message.text, "Hello user", "Welcome message is incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()