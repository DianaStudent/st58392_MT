from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def generate_random_email(self):
        random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"
        return random_email

    def test_user_registration(self):
        driver = self.driver

        # Navigate to login page
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to login page: {str(e)}")

        # Navigate to registration page
        try:
            create_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            create_account_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to registration page: {str(e)}")

        # Fill registration form
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            ).send_keys("Test")
            driver.find_element(By.ID, "field-lastname").send_keys("User")
            driver.find_element(By.ID, "field-email").send_keys(self.generate_random_email())
            driver.find_element(By.ID, "field-password").send_keys("test@user1")

            # Check all checkboxes
            driver.find_element(By.NAME, "psgdpr").click()
            driver.find_element(By.NAME, "customer_privacy").click()

            # Submit the registration form
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        except Exception as e:
            self.fail(f"Failed to fill registration form or submit: {str(e)}")

        # Confirm registration success by checking for 'Sign out'
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign out"))
            )
        except Exception as e:
            self.fail(f"Registration not successful, 'Sign out' not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()