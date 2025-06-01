import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://example.com"  # Replace with the actual URL of the homepage

    def generate_email(self):
        """Generate a random email address."""
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{random_string}@example.com"

    def test_register(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage
        driver.get(self.base_url)

        # Step 2: Click the "Register" link
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        if not register_link or not register_link.is_displayed():
            self.fail("Register link is not found")

        register_link.click()

        # Step 3: Wait for the registration page to load
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "registration-page")))

        # Step 4: Fill all the fields
        # Select Gender
        gender_female_radio = wait.until(EC.visibility_of_element_located((By.ID, "gender-female")))
        if not gender_female_radio or not gender_female_radio.is_displayed():
            self.fail("Gender radio button for Female is not found")

        gender_female_radio.click()

        # First Name
        first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
        if not first_name_field or not first_name_field.is_displayed():
            self.fail("First Name field is not found")

        first_name_field.send_keys("Test")

        # Last Name
        last_name_field = wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
        if not last_name_field or not last_name_field.is_displayed():
            self.fail("Last Name field is not found")

        last_name_field.send_keys("User")

        # Email
        email = self.generate_email()
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        if not email_field or not email_field.is_displayed():
            self.fail("Email field is not found")

        email_field.send_keys(email)

        # Company
        company_field = wait.until(EC.visibility_of_element_located((By.ID, "Company")))
        if not company_field or not company_field.is_displayed():
            self.fail("Company field is not found")

        company_field.send_keys("TestCorp")

        # Password
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        if not password_field or not password_field.is_displayed():
            self.fail("Password field is not found")

        password_field.send_keys("test11")

        # Confirm Password
        confirm_password_field = wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        if not confirm_password_field or not confirm_password_field.is_displayed():
            self.fail("Confirm Password field is not found")

        confirm_password_field.send_keys("test11")

        # Step 5: Submit the registration form
        register_button = wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        if not register_button or not register_button.is_displayed():
            self.fail("Register button is not found")

        register_button.click()

        # Step 6: Verify that a message like "Your registration completed" is shown
        result_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "result")))
        if not result_message or not result_message.is_displayed():
            self.fail("Result message is not found")

        self.assertIn("Your registration completed", result_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()