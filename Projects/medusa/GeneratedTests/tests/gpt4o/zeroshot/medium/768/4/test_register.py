import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class MedusaStoreRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")

    def generate_unique_email(self):
        return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@test.com"

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" link
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        self.assertTrue(account_link, "Account link not found")
        account_link.click()

        # Step 3: Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        self.assertTrue(join_us_button, "Join Us button not found")
        join_us_button.click()

        # Step 4: Fill in all fields for registration
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")

        self.assertTrue(first_name_input and last_name_input and email_input and password_input, "One or more input fields are missing")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        unique_email = self.generate_unique_email()
        email_input.send_keys(unique_email)
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        self.assertTrue(register_button, "Register button not found")
        register_button.click()

        # Step 6: Verify registration success by checking presence of welcome message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        self.assertTrue(welcome_message, "Welcome message not found")
        self.assertIn("Hello user", welcome_message.text, "Welcome message does not contain expected text")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()