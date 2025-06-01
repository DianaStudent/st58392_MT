import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Open the homepage
        driver.get("http://localhost:8000/dk")

        # Step 2: Click the "Account" link.
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Step 3: Click the "Join Us" button.
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        join_us_button.click()

        # Step 4: Fill in all fields.
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']")))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        random_email = f"user_{random.randint(1000,9999)}@test.com"
        email_input.send_keys(random_email)
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form.
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        register_button.click()

        # Step 6: Verify registration success.
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        customer_email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='customer-email']")))

        if not welcome_message or not customer_email:
            self.fail("Registration failed: Welcome message or customer email not found.")

        self.assertIn("Hello user", welcome_message.text)
        self.assertIn(random_email, customer_email.get_attribute("data-value"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()