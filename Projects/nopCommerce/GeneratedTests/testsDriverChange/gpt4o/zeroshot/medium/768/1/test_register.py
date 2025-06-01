import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://max/"

    def random_email(self):
        """
        Generate a random email address
        """
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@example.com"

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Step 2: Click the "Register"
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link not found or not clickable.")

        # Step 3: Wait for the registration page to load
        try:
            page_title = WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Register")
            )
        except:
            self.fail("Registration page did not load properly.")

        # Step 4: Fill all the fields
        try:
            gender_female = driver.find_element(By.ID, "gender-female")
            gender_female.click()

            first_name = driver.find_element(By.ID, "FirstName")
            first_name.send_keys("Test")

            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("User")

            email = driver.find_element(By.ID, "Email")
            email.send_keys(self.random_email())

            company = driver.find_element(By.ID, "Company")
            company.send_keys("TestCorp")

            password = driver.find_element(By.ID, "Password")
            password.send_keys("test11")

            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password.send_keys("test11")
        except:
            self.fail("One or more registration fields not found.")

        # Step 5: Submit the registration form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button not found or not clickable.")

        # Step 6: Verify success message
        try:
            registration_result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            self.assertIn("Your registration completed", registration_result.text)
        except:
            self.fail("Registration success message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()