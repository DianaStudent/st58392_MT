from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from email.utils import parseaddr
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Assuming 'http://max/' is the homepage url

    def generate_email(self):
        return f"testuser_{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}@example.com"

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Register Page
        try:
            my_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        except Exception:
            self.fail("My account link not found or not present in top menu.")
        
        my_account_link.click()

        # Wait for the registration page to load
        try:
            registration_title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']")))
        except Exception:
            self.fail("Registration page did not load as expected.")

        # Fill registration form
        try:
            gender_female = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
            first_name = driver.find_element(By.ID, "FirstName")
            last_name = driver.find_element(By.ID, "LastName")
            email = driver.find_element(By.ID, "Email")
            company = driver.find_element(By.ID, "Company")
            password = driver.find_element(By.ID, "Password")
            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
        except Exception:
            self.fail("One or more form fields are not available.")

        gender_female.click()
        first_name.send_keys("Test")
        last_name.send_keys("User")
        reg_email = self.generate_email()
        email.send_keys(reg_email)
        company.send_keys("TestCorp")
        password.send_keys("test11")
        confirm_password.send_keys("test11")

        # Submit the form
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
        except Exception:
            self.fail("Register button is not clickable or not found.")
        
        register_button.click()

        # Validate registration success
        try:
            confirmation_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            self.assertIsNotNone(confirmation_message)
            self.assertIn("Your registration completed", confirmation_message.text)
        except Exception:
            self.fail("Registration did not complete successfully or confirmation message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()