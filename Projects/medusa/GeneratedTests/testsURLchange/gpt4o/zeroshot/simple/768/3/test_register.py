import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver

        # Go to Account page
        nav_account_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        nav_account_link.click()
        
        # Click on Join us button
        join_us_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[data-testid='register-button']")))
        join_us_button.click()

        # Fill registration form
        first_name_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        first_name_input.send_keys("user")

        last_name_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-testid='last-name-input']")))
        last_name_input.send_keys("test")

        email_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-testid='email-input']")))
        email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(email)

        password_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-testid='password-input']")))
        password_input.send_keys("testuser")

        # Submit the registration form
        register_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[data-testid='register-button']")))
        register_button.click()

        # Confirm success
        welcome_message = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        
        if not welcome_message:
            self.fail("Registration failed: Welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()