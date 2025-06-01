import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

    def test_registration(self):
        driver = self.driver

        # Click on 'Register' link in the header menu
        try:
            register_link = driver.find_element(By.LINK_TEXT, "Register")
        except:
            self.fail("Register link not found on home page")
        register_link.click()

        # Fill personal details
        email = self.random_email()
        
        try:
            gender_male_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-male")))
            gender_male_radio.click()

            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("User")

            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(email)
        except:
            self.fail("One of the personal details fields was not found")

        # Fill company details
        try:
            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("Test Company")
        except:
            self.fail("Company input field was not found")

        # Fill password details
        try:
            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")

            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")
        except:
            self.fail("One of the password fields was not found")

        # Submit registration
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button was not found")

        # Confirm registration success message
        try:
            success_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result' and text()='Your registration completed']"))
            )
            self.assertIn("Your registration completed", success_message.text)
        except:
            self.fail("Registration success message was not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()