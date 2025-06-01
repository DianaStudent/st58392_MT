import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        # Generate a random email
        return ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage and click on "Register" link
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Registration link not found: {str(e)}")

        # Step 2: Wait for the registration form to load
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".registration-page h1")))
        except Exception as e:
            self.fail(f"Registration form did not load: {str(e)}")

        # Step 3: Fill out the registration form
        email = self.generate_email()

        try:
            female_radio = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
            female_radio.click()
        except Exception as e:
            self.fail(f"Gender radio button not found: {str(e)}")

        fields = {
            "FirstName": "Test",
            "LastName": "User",
            "Email": email,
            "Company": "TestCorp",
            "Password": "test11",
            "ConfirmPassword": "test11"
        }

        for field_id, value in fields.items():
            try:
                field_elem = wait.until(EC.presence_of_element_located((By.ID, field_id)))
                field_elem.send_keys(value)
            except Exception as e:
                self.fail(f"Field {field_id} could not be filled: {str(e)}")

        # Step 4: Submit the registration form
        try:
            register_button = wait.until(EC.presence_of_element_located((By.ID, "register-button")))
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found or could not be clicked: {str(e)}")

        # Step 5: Verify registration success
        try:
            success_message_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
            self.assertIn("Your registration completed", success_message_elem.text)
        except Exception as e:
            self.fail(f"Registration success message not found or incorrect: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()