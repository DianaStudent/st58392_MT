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

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")  # replace with the actual homepage URL

    def generate_email(self):
        # Generate a random email address
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@example.com"

    def test_register_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Step 2: Click the "Register"
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()

            # Step 3: Wait for the registration page to load
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

            # Step 4: Fill all the fields
            # Select Female
            gender_female = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
            gender_female.click()

            # Fill in First Name
            first_name = driver.find_element(By.ID, "FirstName")
            self.assertIsNotNone(first_name, "First name input was not found.")
            first_name.send_keys("Test")

            # Fill in Last Name
            last_name = driver.find_element(By.ID, "LastName")
            self.assertIsNotNone(last_name, "Last name input was not found.")
            last_name.send_keys("User")

            # Fill in Email
            email = driver.find_element(By.ID, "Email")
            self.assertIsNotNone(email, "Email input was not found.")
            generated_email = self.generate_email()
            email.send_keys(generated_email)

            # Fill in Company
            company = driver.find_element(By.ID, "Company")
            self.assertIsNotNone(company, "Company input was not found.")
            company.send_keys("TestCorp")

            # Fill in Password
            password = driver.find_element(By.ID, "Password")
            self.assertIsNotNone(password, "Password input was not found.")
            password.send_keys("test11")

            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            self.assertIsNotNone(confirm_password, "Confirm password input was not found.")
            confirm_password.send_keys("test11")

            # Step 5: Submit the registration form
            register_button = driver.find_element(By.ID, "register-button")
            self.assertIsNotNone(register_button, "Register button was not found.")
            register_button.click()

            # Step 6: Verify success message
            success_message = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            self.assertIsNotNone(success_message, "Success message element was not found.")
            self.assertIn("Your registration completed", success_message.text)

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()