from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        
        # Step 1: Navigate to the login page
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found: {e}")

        # Step 3: Click on the register link
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found: {e}")

        # Step 4: Fill in the registration form
        try:
            # Gender
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            ).click()

            # First Name
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            ).send_keys("Test")

            # Last Name
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            ).send_keys("User")

            # Email
            email = f"test_{random.randint(100000, 999999)}@user.com"
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            ).send_keys(email)

            # Password
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            ).send_keys("test@user1")

            # Birthdate
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            ).send_keys("05/31/1990")

            # Step 5: Check required checkboxes
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "optin"))
            ).click()
            
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            ).click()

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "newsletter"))
            ).click()
            
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            ).click()

            # Step 6: Submit the form
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.form-control-submit"))
            ).click()

        except Exception as e:
            self.fail(f"Error filling registration form: {e}")

        # Step 7: Confirm success
        try:
            sign_out_text = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out_text, "Registration was not successful.")
        except Exception as e:
            self.fail(f"Sign out not found, registration failed: {e}")

if __name__ == "__main__":
    unittest.main()