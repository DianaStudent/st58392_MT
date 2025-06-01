import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open homepage and click "Register" link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_link, "Register link not found.")
        register_link.click()

        # Wait for the registration page to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "registration-page")))

        # Fill in registration form details
        gender_female = driver.find_element(By.ID, "gender-female")
        first_name = driver.find_element(By.ID, "FirstName")
        last_name = driver.find_element(By.ID, "LastName")
        email_field = driver.find_element(By.ID, "Email")
        company_name = driver.find_element(By.ID, "Company")
        password_field = driver.find_element(By.ID, "Password")
        confirm_password = driver.find_element(By.ID, "ConfirmPassword")
        
        self.assertIsNotNone(gender_female, "Gender field not found.")
        self.assertIsNotNone(first_name, "First name field not found.")
        self.assertIsNotNone(last_name, "Last name field not found.")
        self.assertIsNotNone(email_field, "Email field not found.")
        self.assertIsNotNone(company_name, "Company field not found.")
        self.assertIsNotNone(password_field, "Password field not found.")
        self.assertIsNotNone(confirm_password, "Confirm Password field not found.")
        
        gender_female.click()
        first_name.send_keys("Test")
        last_name.send_keys("User")
        
        # Generate a random email
        random_email = f"testuser{''.join(random.choice(string.ascii_letters) for _ in range(6))}@example.com"
        email_field.send_keys(random_email)
        
        company_name.send_keys("TestCorp")
        password_field.send_keys("test11")
        confirm_password.send_keys("test11")

        # Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        self.assertIsNotNone(register_button, "Register button not found.")
        register_button.click()

        # Verify successful registration
        success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        self.assertIsNotNone(success_message, "Success message not found.")
        self.assertIn("Your registration completed", success_message.text, "Registration not completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()