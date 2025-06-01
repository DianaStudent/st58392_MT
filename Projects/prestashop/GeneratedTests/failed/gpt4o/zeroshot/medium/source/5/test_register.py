from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver

        # Step 1: Click on the login link
        login_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']")))
        login_link.click()

        # Step 2: Click on the register link on the login page
        register_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        register_link.click()

        # Step 3: Fill in registration form fields
        # Gender
        gender_radio = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='field-id_gender-1']")))
        gender_radio.click()
        
        # First name
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        first_name_field.send_keys("Test")

        # Last name
        last_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        last_name_field.send_keys("User")

        # Email
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        email_field.send_keys(f"test_{random.randint(100000,999999)}@user.com")

        # Password
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        password_field.send_keys("test@user1")

        # Birthday
        birthday_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-birthday")))
        birthday_field.send_keys("05/31/1990")

        # Step 4: Check required checkboxes
        optin_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "optin")))
        optin_checkbox.click()

        customer_privacy_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer_privacy")))
        customer_privacy_checkbox.click()

        terms_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "psgdpr")))
        terms_checkbox.click()

        # Submit the form
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Save')]")))
        submit_button.click()

        # Step 5: Confirm success by checking presence of "Sign out"
        sign_out_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='logout hidden-sm-down']")))
        self.assertIn("Sign out", sign_out_link.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()