import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class MedusaStoreRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8000/dk')
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = ActionChains(self.driver)

    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return f"user_{random_string}@test.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Navigate to account page
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_link.click()

        # Go to registration form
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        register_button.click()

        # Fill registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        email_input.send_keys(self.generate_random_email())

        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        password_input.send_keys("testuser")

        # Submit the form
        join_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        join_button.click()

        # Confirm registration success
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        self.assertIn("Hello user", welcome_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()