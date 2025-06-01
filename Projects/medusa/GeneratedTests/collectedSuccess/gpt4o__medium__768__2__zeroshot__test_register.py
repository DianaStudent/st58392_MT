import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver

        # Step 2: Click the "Account" link
        account_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]'))
        )
        account_link.click()

        # Step 3: Click the "Join us" button
        join_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]'))
        )
        join_button.click()

        # Step 4: Fill in all fields
        first_name_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]'))
        )
        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')

        first_name = "user"
        last_name = "test"
        email = f"user_{int(time.time())}@test.com"  # dynamically generated email
        password = "testuser"

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        password_input.send_keys(password)

        # Step 5: Submit the registration form
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="register-button"]'))
        )
        submit_button.click()

        # Step 6: Verify registration success
        welcome_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'))
        )

        # Confirm if the welcome message is present and not empty
        self.assertIsNotNone(welcome_message, "Welcome message not found.")
        self.assertNotEqual(welcome_message.text.strip(), "", "Welcome message is empty.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()