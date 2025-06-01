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
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Navigate to registration page (assuming it's accessible via a link, but it's not present in provided html.
        # So, directly navigating to /register. This might need adjustment based on actual site structure.)
        driver.get("http://max/register")

        # Verify that the registration page is loaded
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-page"))
            )
        except:
            self.fail("Registration page did not load correctly.")

        # Generate a random email address
        random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        email = f"test_{random_string}@example.com"

        # Locate elements using selectors from html_data and fill the registration form
        try:
            # Gender
            male_radio = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            )
            male_radio.click()

            # First Name
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name_input.send_keys("John")

            # Last Name
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name_input.send_keys("Doe")

            # Email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys(email)

            # Company (optional)
            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys("Test Company")

            # Newsletter (already checked by default)

            # Password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("test11")

            # Confirm Password
            confirm_password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password_input.send_keys("test11")

            # Register Button
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )
            register_button.click()

        except Exception as e:
            self.fail(f"Failed to fill registration form: {e}")

        # Verify successful registration
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
            )
            result_message = driver.find_element(By.CLASS_NAME, "result").text
            self.assertEqual(result_message, "Your registration completed")

        except Exception as e:
            self.fail(f"Registration failed or success message not found: {e}")


if __name__ == "__main__":
    unittest.main()