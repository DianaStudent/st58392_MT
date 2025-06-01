import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        return f"testuser{random.randint(1000, 9999)}@example.com"

    def test_register_user(self):
        driver = self.driver

        # Step 1: Open the homepage
        driver.get("http://max/")
        
        # Step 2: Click the "Register" link in the top navigation
        register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()
        
        # Step 3: Wait for the registration form to load
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

        # Step 4: Select the appropriate gender radio input (Female)
        gender_female = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        gender_female.click()
        
        # Step 5: Fill in all required fields
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        last_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "LastName")))
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
        company_input = self.wait.until(EC.presence_of_element_located((By.ID, "Company")))
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "Password")))
        confirm_password_input = self.wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email = self.generate_email()
        email_input.send_keys(email)
        company_input.send_keys("TestCorp")
        password_input.send_keys("test11")
        confirm_password_input.send_keys("test11")

        # Step 6: Submit the registration form
        register_button = self.wait.until(EC.presence_of_element_located((By.ID, "register-button")))
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load
        result_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))

        # Step 8: Verify that registration succeeded
        if not result_message or "Your registration completed" not in result_message.text:
            self.fail("Registration failed or confirmation message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()