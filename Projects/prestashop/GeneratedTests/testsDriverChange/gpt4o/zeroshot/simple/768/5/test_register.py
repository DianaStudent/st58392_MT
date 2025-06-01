import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to sign in page
        sign_in_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        )
        sign_in_link.click()

        # Click on create account
        create_account_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
        )
        create_account_link.click()
        
        # Fill out the registration form
        # Social title
        mr_radio = wait.until(
            EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
        )
        mr_radio.click()

        # First name
        first_name_input = wait.until(
            EC.visibility_of_element_located((By.ID, "field-firstname"))
        )
        first_name_input.send_keys("Test")

        # Last name
        last_name_input = driver.find_element(By.ID, "field-lastname")
        last_name_input.send_keys("User")

        # Email
        email_input = driver.find_element(By.ID, "field-email")
        random_email = "user_" + ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"
        email_input.send_keys(random_email)

        # Password
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        # Opt-in, terms, and privacy checkboxes
        optin_checkbox = driver.find_element(By.NAME, "optin")
        if not optin_checkbox.is_selected():
            optin_checkbox.click()

        psgdpr_checkbox = driver.find_element(By.NAME, "psgdpr")
        if not psgdpr_checkbox.is_selected():
            psgdpr_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        if not newsletter_checkbox.is_selected():
            newsletter_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        if not privacy_checkbox.is_selected():
            privacy_checkbox.click()

        # Submit the form
        save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_button.click()

        # Confirm registration by checking for "Sign out" link
        try:
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertIsNotNone(sign_out_link, "Sign out link should appear on successful registration.")
        except:
            self.fail("Registration failed or Sign out link wasn't found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()