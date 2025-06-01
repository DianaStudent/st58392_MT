from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def generate_email(self):
        return f"test_{int(time.time())}@example.com"

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the registration page
        sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        registration_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        registration_link.click()

        # Fill the registration form
        first_name_input = wait.until(EC.element_to_be_clickable((By.ID, "field-firstname")))
        last_name_input = driver.find_element(By.ID, "field-lastname")
        email_input = driver.find_element(By.ID, "field-email")
        password_input = driver.find_element(By.ID, "field-password")
        
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys(self.generate_email())
        password_input.send_keys("test@user1")

        # Check the required checkboxes
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        customer_privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        
        if not terms_checkbox.is_selected():
            terms_checkbox.click()
        if not customer_privacy_checkbox.is_selected():
            customer_privacy_checkbox.click()

        # Submit the form
        save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_button.click()

        # Verify registration success
        sign_out_text = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign out")))
        if not sign_out_text:
            self.fail("Sign out link not found - registration might have failed.")
        
        self.assertTrue(sign_out_text.is_displayed(), "User is not registered successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()