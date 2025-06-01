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

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "Register" link
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link is not present or not clickable.")

        # Wait for registration page to load
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form[action='/register?returnurl=%2F']")))
        except:
            self.fail("Registration page did not load correctly.")
        
        # Fill form
        try:
            gender_female = driver.find_element(By.ID, "gender-female")
            gender_female.click()

            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("User")

            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(self.generate_dynamic_email())

            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("TestCorp")

            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")

            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")
        except:
            self.fail("Failed to fill the registration form.")

        # Submit form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button is not present or not clickable.")

        # Verify registration success
        try:
            result_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
            self.assertIn("Your registration completed", result_message.text)
        except:
            self.fail("Registration was not successful or success message not found.")
    
    def generate_dynamic_email(self):
        # Generate a dynamic email for testing
        domain = "example.com"
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{random_string}@{domain}"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()