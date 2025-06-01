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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Navigate to registration page (assuming it's accessible via a link, but the provided HTML doesn't show it.  Adding a placeholder for navigation)
        # In a real scenario, you'd need to find the actual registration link and click it.
        # For now, we'll just navigate directly to /register if that's the correct URL.  If not, the test will fail.
        driver.get("http://max/register")

        # Wait for the registration form to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "register-button"))
        )

        # Generate a random email address
        random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        email = f"test_{random_string}@example.com"

        # Fill in the registration form
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

            # Company (optional, but filling it in)
            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_input.send_keys("Test Company")

            # Newsletter (already checked, but let's explicitly check it anyway)
            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Newsletter"))
            )
            if not newsletter_checkbox.is_selected():
                newsletter_checkbox.click()

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
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()

            # Wait for the registration result page to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "registration-result-page"))
            )

            # Verify success message
            result_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            ).text
            self.assertEqual("Your registration completed", result_message)

        except Exception as e:
            self.fail(f"An error occurred during registration: {e}")


if __name__ == "__main__":
    unittest.main()