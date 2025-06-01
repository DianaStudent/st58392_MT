import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Click the "Account" link
        account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 2. Click the "Join us" button
        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        if register_button:
            register_button.click()
        else:
            self.fail("Join us button not found")

        # 3. Fill in the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        last_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']")))
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))

        if not all([first_name_input, last_name_input, email_input, password_input]):
            self.fail("One or more input fields not found")
        
        unique_id = str(uuid.uuid4())
        email = f"user_{unique_id}@test.com"

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(email)
        password_input.send_keys("testuser")

        # 4. Submit the registration form
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 5. Verify registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        if welcome_message:
            welcome_text = welcome_message.text
            self.assertIn("Hello user", welcome_text, "Welcome message not found")
        else:
            self.fail("Welcome message element not found")

if __name__ == "__main__":
    unittest.main()