import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        
        # Navigate to Account Page
        account_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Click Register Button
        register_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        register_button.click()

        # Fill the registration form
        self.fill_registration_form(driver)

        # Submit the form
        submit_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        submit_button.click()
        
        # Verify Registration Success
        try:
            welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail("Registration did not succeed. Welcome message not found.")

    def fill_registration_form(self, driver):
        try:
            first_name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
            last_name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']")))
            email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))

            # Fill inputs
            first_name_input.send_keys("user")
            last_name_input.send_keys("test")
            email_input.send_keys(f"user_{str(int(time.time()))}@test.com")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to fill registration form: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()