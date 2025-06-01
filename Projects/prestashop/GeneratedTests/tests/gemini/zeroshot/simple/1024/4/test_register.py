import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Go to Sign in page
        try:
            sign_in_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except:
            self.fail("Could not find 'Sign in' link on the home page.")

        # 2. Go to registration page
        try:
            create_account_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
            )
            create_account_link.click()
        except:
            self.fail("Could not find 'Create account' link on the login page.")

        # 3. Fill registration form
        # Generate random email
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        email = f"test_{random_string}@example.com"

        try:
            # Select social title
            mr_radio = wait.until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Fill first name
            firstname_input = wait.until(
                EC.visibility_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")

            # Fill last name
            lastname_input = wait.until(
                EC.visibility_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")

            # Fill email
            email_input = wait.until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(email)

            # Fill password
            password_input = wait.until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys("test@user1")

            # Check all checkboxes
            psgdpr_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            newsletter_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "newsletter"))
            )
            newsletter_checkbox.click()

            customer_privacy_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

        except:
            self.fail("Could not fill the registration form.")

        # 4. Submit the form
        try:
            save_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Save')]"))
            )
            save_button.click()
        except:
            self.fail("Could not submit the registration form.")

        # 5. Verify successful registration
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Sign out')]"))
            )
        except:
            self.fail("Registration failed. 'Sign out' link not found.")

if __name__ == "__main__":
    unittest.main()