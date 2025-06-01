from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Replace with the actual register page URL

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        # Wait for the registration form to become visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "form"))
        )

        try:
            # Fill Gender
            male_radio = driver.find_element(By.ID, "gender-male")
            male_radio.click()

            # Fill First Name
            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("Test")

            # Fill Last Name
            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("User")

            # Generate a dynamic email
            random_email = f"testuser{random.randint(1000, 9999)}@example.com"

            # Fill Email
            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(random_email)

            # Fill Password
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")

            # Fill Confirm Password
            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")

            # Submit the registration form
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

            # Wait for the registration result page to be visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "result"))
            )

            # Confirm registration success
            registration_result = driver.find_element(By.CLASS_NAME, "result").text
            self.assertIn("Your registration completed", registration_result)

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

if __name__ == "__main__":
    unittest.main()