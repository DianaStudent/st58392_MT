import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage (already opened in setUp)
        
        # Step 2: Click the login link
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: Click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 4: Fill registration form
        # Generating a dynamic email
        dynamic_email = f"test_{random.randint(100000, 999999)}@user.com"

        # Fill form fields
        gender_radio = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_radio.click()

        first_name_field = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        first_name_field.send_keys("Test")

        last_name_field = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        last_name_field.send_keys("User")

        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_field.send_keys(dynamic_email)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_field.send_keys("test@user1")

        birthday_field = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday_field.send_keys("01/01/2000")

        # Step 5: Tick all checkboxes
        privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        privacy_checkbox.click()

        terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        terms_checkbox.click()

        newsletter_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "newsletter")))
        newsletter_checkbox.click()

        # Step 6: Submit the registration form
        save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        save_button.click()

        # Step 7: Wait for the redirect after login
        time.sleep(3)  # This is often too implicit and should be handled with waits.

        # Step 8: Check for successful login
        try:
            signout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            account_name = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Test User')]")))

            self.assertIsNotNone(signout_button, "Sign out button not found, login may not be successful")
            self.assertIsNotNone(account_name, "User name not found in account info")
        
        except:
            self.fail("Test failed, registration was not successful")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()