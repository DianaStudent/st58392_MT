import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # Navigate to registration page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("Could not find 'My account' link.")

        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Could not find 'Register' link.")

        # Fill in registration form
        try:
            gender_male = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "gender-male"))
            )
            gender_male.click()
        except:
            self.fail("Could not find 'gender-male' radio button.")

        try:
            first_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "FirstName"))
            )
            first_name.send_keys("John")
        except:
            self.fail("Could not find 'FirstName' input field.")

        try:
            last_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "LastName"))
            )
            last_name.send_keys("Doe")
        except:
            self.fail("Could not find 'LastName' input field.")

        email = "test" + str(random.randint(1, 100000)) + "@example.com"
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_field.send_keys(email)
        except:
            self.fail("Could not find 'Email' input field.")

        try:
            company_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Company"))
            )
            company_name.send_keys("Acme Corp")
        except:
            self.fail("Could not find 'Company' input field.")

        try:
            password = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password.send_keys("test11")
        except:
            self.fail("Could not find 'Password' input field.")

        try:
            confirm_password = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ConfirmPassword"))
            )
            confirm_password.send_keys("test11")
        except:
            self.fail("Could not find 'ConfirmPassword' input field.")

        # Submit the form
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register_button.click()
        except:
            self.fail("Could not find 'register-button'.")

        # Verify registration success
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='result'][contains(text(), 'Your registration completed')]"))
            )
        except:
            self.fail("Registration failed. Success message not found.")

if __name__ == "__main__":
    unittest.main()