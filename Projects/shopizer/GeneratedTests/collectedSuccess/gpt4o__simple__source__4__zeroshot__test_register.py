import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found: {e}")

        # Navigate to registration page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            register_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_button.click()
        except Exception as e:
            self.fail(f"Navigation to registration page failed: {e}")
        
        # Fill registration form
        email = self.generate_random_email()
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            repeat_password_input = wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
            first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
            country_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select")))
            state_select = wait.until(EC.presence_of_element_located((By.XPATH, "(//select)[2]")))
            register_submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

            email_input.send_keys(email)
            password_input.send_keys("test**11")
            repeat_password_input.send_keys("test**11")
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            country_select.send_keys(Keys.ARROW_DOWN + Keys.RETURN)  # Selecting Canada
            state_select.send_keys("Quebec" + Keys.RETURN)

            register_submit_button.click()
        except Exception as e:
            self.fail(f"Filling registration form failed: {e}")
        
        # Validate account creation
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Registration success not confirmed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()