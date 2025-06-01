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
        self.driver.get("http://max/")
    
    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com"

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click the "Register" link
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link is not available.")

        # Wait for registration page and fill out the form
        try:
            wait.until(EC.presence_of_element_located((By.ID, "register-button")))

            gender_female_radio = driver.find_element(By.ID, "gender-female")
            gender_female_radio.click()

            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("User")

            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(self.generate_random_email())

            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("TestCorp")

            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")

            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")

            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("The registration form is not properly loaded or filled.")

        # Verify registration success
        try:
            result_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            self.assertIn("Your registration completed", result_message.text)
        except:
            self.fail("Registration success message is not displayed.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()