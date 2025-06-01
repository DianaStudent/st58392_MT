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

    def tearDown(self):
        self.driver.quit()

    def generate_email(self):
        return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"

    def test_user_registration(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/registration")

        # Wait for registration form
        self.wait_until_visible(By.ID, "customer-form")

        try:
            # Fill the registration form
            first_name_field = self.find_element(By.ID, "field-firstname")
            first_name_field.send_keys("Test")

            last_name_field = self.find_element(By.ID, "field-lastname")
            last_name_field.send_keys("User")

            email_field = self.find_element(By.ID, "field-email")
            email_field.send_keys(self.generate_email())

            password_field = self.find_element(By.ID, "field-password")
            password_field.send_keys("test@user1")

            # Check required checkboxes
            psgdpr_checkbox = self.find_element(By.NAME, "psgdpr")
            psgdpr_checkbox.click()

            customer_privacy_checkbox = self.find_element(By.NAME, "customer_privacy")
            customer_privacy_checkbox.click()

            # Submit the registration form
            submit_button = self.find_element(By.CSS_SELECTOR, "button[type=submit]")
            submit_button.click()

            # Wait for the home page to be visible
            self.wait_until_visible(By.ID, "index")

            # Verify registration success by checking "Sign out" link
            self.wait_until_visible(By.LINK_TEXT, "Sign out")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def wait_until_visible(self, by, value):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((by, value)))

    def find_element(self, by, value):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((by, value)))
        if not element:
            self.fail(f"Element not found: {value}")
        return element

if __name__ == "__main__":
    unittest.main()