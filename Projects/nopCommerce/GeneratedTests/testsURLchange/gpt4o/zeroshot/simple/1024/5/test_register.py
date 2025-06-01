import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver

        # Navigate to the registration page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'My account' link: {str(e)}")

        # Fill in registration details
        try:
            gender_male = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            )
            gender_male.click()
            
            first_name = driver.find_element(By.ID, "FirstName")
            first_name.send_keys("John")
            
            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("Doe")
            
            email = driver.find_element(By.ID, "Email")
            email_address = f"testuser{random.randint(1000, 9999)}@example.com"
            email.send_keys(email_address)
            
            password = driver.find_element(By.ID, "Password")
            password.send_keys("test11")
            
            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password.send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to fill registration form: {str(e)}")

        # Submit the registration form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Register' button: {str(e)}")

        # Confirm registration success
        try:
            registration_success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
            self.assertIn("Your registration completed", registration_success_message.text)
        except Exception as e:
            self.fail(f"Registration success message not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()