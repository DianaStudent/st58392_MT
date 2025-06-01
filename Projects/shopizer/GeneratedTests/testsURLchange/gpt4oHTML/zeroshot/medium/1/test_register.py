import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def generate_email(self):
        # Generate a random email
        domains = ["@example.com", "@test.com", "@sample.org"]
        prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return prefix + random.choice(domains)

    def test_registration(self):
        driver = self.driver
        driver.get("http://localhost/")  # Use your local server URL or change to the real URL

        # Accept cookies
        try:
            accept_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable.")
        
        # Navigate to Registration Page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Account button or Register link not found or not clickable.")

        # Fill out registration form
        try:
            email = self.generate_email()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            ).send_keys(email)

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "password"))
            ).send_keys("test**11")

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "repeatPassword"))
            ).send_keys("test**11")

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "firstName"))
            ).send_keys("Test")

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "lastName"))
            ).send_keys("User")

            # Select country and state
            country_select = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//select/option[text()='Canada']"))
            )
            country_select.click()

            state_select = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//select/option[text()='Quebec']"))
            )
            state_select.click()

            # Submit the registration form
            submit_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span='Register']"))
            )
            submit_button.click()
        except:
            self.fail("Failed to fill out registration form.")

        # Confirm registration success
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Redirection to '/my-account' failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()