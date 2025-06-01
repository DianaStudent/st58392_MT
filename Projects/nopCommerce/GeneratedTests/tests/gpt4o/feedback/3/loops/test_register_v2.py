import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        
    def tearDown(self):
        self.driver.quit()
    
    def generate_email(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10)) + "@example.com"

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Register" link in the top navigation
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception:
            self.fail("Register link was not found")

        # Step 3: Wait for the registration form to load
        try:
            page_title = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1"))
            )
            self.assertTrue(page_title and page_title.text == "Register", "Registration page did not load properly")
        except Exception:
            self.fail("Registration page title was not found or is incorrect")

        # Step 4: Select the appropriate gender radio input
        try:
            gender_female = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
            gender_female.click()
        except Exception:
            self.fail("Gender radio button was not found or not clickable")
        
        # Step 5: Fill in all required fields
        try:
            first_name_input = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
            first_name_input.send_keys("Test")
            
            last_name_input = wait.until(EC.presence_of_element_located((By.ID, "LastName")))
            last_name_input.send_keys("User")

            email = self.generate_email()
            email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            email_input.send_keys(email)
            
            company_input = wait.until(EC.presence_of_element_located((By.ID, "Company")))
            company_input.send_keys("TestCorp")
            
            password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
            password_input.send_keys("test11")
            
            confirm_password_input = wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))
            confirm_password_input.send_keys("test11")
        except Exception:
            self.fail("Failed to fill one or more form fields")

        # Step 6: Submit the registration form
        try:
            register_button = wait.until(EC.presence_of_element_located((By.ID, "register-button")))
            register_button.click()
        except Exception:
            self.fail("Register button was not found or not clickable")

        # Step 7: Wait for the response page or confirmation message to load
        try:
            confirmation_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and text()='Your registration completed']"))
            )
        except Exception:
            self.fail("Confirmation message was not found or is incorrect")

        # Step 8: Verify that registration succeeded
        self.assertIsNotNone(confirmation_message, "Confirmation message not found")
        self.assertIn("Your registration completed", confirmation_message.text, "Registration failed or incorrect message")

if __name__ == "__main__":
    unittest.main()