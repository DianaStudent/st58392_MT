import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import string

class MedusaStoreRegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.get("http://localhost:8000/dk")

    def generate_email(self):
        return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@test.com"

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get("http://localhost:8000/dk")

        # Step 2: Click the "Account" link.
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Step 3: Click the "Join Us" button.
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        join_us_button.click()

        # Step 4: Fill in all fields: first name, last name, email (generate it unique), password.
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")

        if not (first_name_input and last_name_input and email_input and password_input):
            self.fail("One or more registration fields are missing")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(self.generate_email())
        password_input.send_keys("testuser")

        # Step 5: Submit the registration form.
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        if not register_button:
            self.fail("Register button is missing")
        register_button.click()

        # Step 6: Verify registration success by checking the presence of welcome message.
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        
        if not welcome_message or not welcome_message.text:
            self.fail("Registration failed or welcome message missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()