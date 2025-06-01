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

    def test_registration(self):
        driver = self.driver

        # Step 1: Open the homepage (already done in setUp)

        # Step 2: Click the "Account" link
        account_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        self.assertTrue(account_link, "Account link is missing")
        account_link.click()

        # Step 3: Click the "Join Us" button
        join_us_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        self.assertTrue(join_us_button, "Join us button is missing")
        join_us_button.click()

        # Step 4: Fill in all fields: first name, last name, email (generate it unique), password
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='register-page']")))

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='first-name-input']")
        self.assertTrue(first_name_input, "First name input is missing")
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        self.assertTrue(last_name_input, "Last name input is missing")
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        self.assertTrue(email_input, "Email input is missing")
        unique_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(unique_email)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        self.assertTrue(password_input, "Password input is missing")
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        self.assertTrue(register_button, "Register button is missing")
        register_button.click()

        # Step 6: Verify registration success by checking presence of welcome message
        welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        self.assertTrue(welcome_message and welcome_message.text.strip(), "Welcome message is missing or empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()