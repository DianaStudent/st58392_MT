from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import string
import random

class TestRegistrationFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_registration_flow(self):
        # Click the "Account" button in the right left corner
        account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='account-button']")))
        account_button.click()

        # Click the "Join Us" button below the login form
        join_us_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='join-us-button']")))
        join_us_button.click()

        # Fill in all fields: first name, last name, and password from credentials, generate unique email.
        first_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='first-name-field']")))
        last_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='last-name-field']")))
        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='email-field']")))
        password_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='password-field']")))

        first_name_field.send_keys("user")
        last_name_field.send_keys("test")
        email_field.send_keys(self.generate_email())
        password_field.send_keys("testuser")

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-button']")))
        submit_button.click()

        # Verify registration success by checking presence of welcome message "Hello user".
        welcome_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@data-testid='welcome-message']")))
        self.assertIsNotNone(welcome_message.text)
        self.assertEqual("Hello user", welcome_message.text)

    def generate_email(self):
        return f"test{random.randint(10000, 99999)}@example.com"

if __name__ == "__main__":
    unittest.main()