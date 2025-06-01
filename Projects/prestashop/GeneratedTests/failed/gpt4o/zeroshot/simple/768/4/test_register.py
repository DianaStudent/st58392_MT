from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Navigate to registration page
        try:
            sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()
            
            create_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
            create_account_link.click()
        except Exception as e:
            self.fail(f"Navigation to registration page failed: {str(e)}")

        try:
            # Fill registration form
            firstname_input = wait.until(EC.element_to_be_clickable((By.ID, "field-firstname")))
            lastname_input = driver.find_element(By.ID, "field-lastname")
            email_input = driver.find_element(By.ID, "field-email")
            password_input = driver.find_element(By.ID, "field-password")

            firstname_input.send_keys("Test")
            lastname_input.send_keys("User")
            email_input.send_keys(f"test_{int(time.time())}@example.com")
            password_input.send_keys("test@user1")

            # Check all checkboxes
            optin_checkbox = driver.find_element(By.NAME, "optin")
            psgdpr_checkbox = driver.find_element(By.NAME, "psgdpr")
            newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
            customer_privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")

            if not optin_checkbox.is_selected():
                optin_checkbox.click()
            if not psgdpr_checkbox.is_selected():
                psgdpr_checkbox.click()
            if not newsletter_checkbox.is_selected():
                newsletter_checkbox.click()
            if not customer_privacy_checkbox.is_selected():
                customer_privacy_checkbox.click()

            # Submit the form
            submit_button = driver.find_element(By.CSS_SELECTOR, ".form-footer .btn-primary")
            submit_button.click()

            # Check for success by finding "Sign out" text
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign out")))
        except Exception as e:
            self.fail(f"Registration failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()