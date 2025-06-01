import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        random_number = random.randint(100000, 999999)
        return f"test_{random_number}@user.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        email = self.generate_email()

        # Step 1: Open the homepage
        driver.get("http://localhost:8080/en/")

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: On the login page, click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 4: Fill in the registration form
        wait.until(EC.presence_of_element_located((By.ID, "customer-form")))
        
        # Gender
        gender_radio = driver.find_element(By.ID, "field-id_gender-1")
        gender_radio.click()

        # First name
        first_name_input = driver.find_element(By.ID, "field-firstname")
        first_name_input.send_keys("Test")

        # Last name
        last_name_input = driver.find_element(By.ID, "field-lastname")
        last_name_input.send_keys("User")

        # Email
        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(email)

        # Password
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        # Birthday
        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("01/01/2000")

        # Step 5: Tick checkboxes for privacy, newsletter, terms, etc.
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        newsletter_checkbox.click()

        # Step 6: Submit the registration form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.form-control-submit")
        submit_button.click()

        # Step 7: Wait for redirect after login
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))

        # Step 8: Confirm that login was successful
        try:
            sign_out_button = driver.find_element(By.LINK_TEXT, "Sign out")
            self.assertTrue(sign_out_button.is_displayed(), "Sign out button not found")
            account_name = driver.find_element(By.CLASS_NAME, "account")
            self.assertIn("Test User", account_name.text, "Username not displayed correctly")
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()