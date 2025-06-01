import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def get_random_email(self):
        return 'test_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '@example.com'

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage (already done in setUp).
        
        # Step 2: Click the "Register" link in the top navigation.
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link not found on the homepage.")
        
        # Step 3 and 4: Wait for the registration form to load and select the gender.
        try:
            gender_female = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
            gender_female.click()
        except:
            self.fail("Gender radio button not found on the registration page.")
        
        # Step 5: Fill in all required fields.
        try:
            first_name = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
            first_name.send_keys("Test")

            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("User")

            # Dynamically generated email
            email_value = self.get_random_email()
            email = driver.find_element(By.ID, "Email")
            email.send_keys(email_value)

            company_name = driver.find_element(By.ID, "Company")
            company_name.send_keys("TestCorp")

            password = driver.find_element(By.ID, "Password")
            password.send_keys("test11")

            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password.send_keys("test11")
        except:
            self.fail("One or more input fields are not found on the registration page.")

        # Step 6: Submit the registration form.
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button not found on the registration page.")
        
        # Step 7 and 8: Wait for the response page and verify success message.
        try:
            registration_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            self.assertIn("Your registration completed", registration_result.text)
        except:
            self.fail("Registration success message not found or incorrect.")

if __name__ == "__main__":
    unittest.main()