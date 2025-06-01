import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Generate a dynamic email
        dynamic_email = "testuser_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@example.com"

        # Step 1: Open the homepage
        self.assertIn("Your store name", driver.title)

        # Step 2: Click the "Register"
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception:
            self.fail("Register link not found.")

        # Step 3: Wait for the registration page to load
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        except Exception:
            self.fail("Registration page did not load.")

        # Step 4: Fill in all the fields
        try:
            gender_female = driver.find_element(By.ID, "gender-female")
            gender_female.click()

            first_name = driver.find_element(By.ID, "FirstName")
            first_name.send_keys("Test")

            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("User")

            email = driver.find_element(By.ID, "Email")
            email.send_keys(dynamic_email)

            company = driver.find_element(By.ID, "Company")
            company.send_keys("TestCorp")

            password = driver.find_element(By.ID, "Password")
            password.send_keys("test11")

            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password.send_keys("test11")
        except Exception:
            self.fail("A form field could not be filled.")

        # Step 5: Submit the registration form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except Exception:
            self.fail("Register button not found.")

        # Step 6: Verify that a message like "Your registration completed" is shown
        try:
            result_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            self.assertIn("Your registration completed", result_message.text)
        except Exception:
            self.fail("Success message not found or registration failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()