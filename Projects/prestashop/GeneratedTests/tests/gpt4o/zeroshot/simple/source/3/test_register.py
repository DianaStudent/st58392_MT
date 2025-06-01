import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        
    def tearDown(self):
        self.driver.quit()

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10)) + "@example.com"

    def test_registration(self):
        driver = self.driver

        # Navigate to the login page
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        )
        sign_in_link.click()

        # Click on "No account? Create one here"
        create_account_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
        )
        create_account_link.click()

        # Fill out registration form
        gender_mr = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input#field-id_gender-1"))
        )
        gender_mr.click()

        first_name = driver.find_element(By.CSS_SELECTOR, "input#field-firstname")
        first_name.send_keys("Test")

        last_name = driver.find_element(By.CSS_SELECTOR, "input#field-lastname")
        last_name.send_keys("User")

        email = driver.find_element(By.CSS_SELECTOR, "input#field-email")
        email.send_keys(self.generate_random_email())

        password = driver.find_element(By.CSS_SELECTOR, "input#field-password")
        password.send_keys("test@user1")

        agree_terms = driver.find_element(By.CSS_SELECTOR, "input[name='psgdpr']")
        agree_terms.click()

        customer_privacy = driver.find_element(By.CSS_SELECTOR, "input[name='customer_privacy']")
        customer_privacy.click()

        # Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, "button.form-control-submit")
        save_button.click()

        # Wait for the user to be logged in and check for "Sign out"
        sign_out = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )
        self.assertIsNotNone(sign_out, "Registration might have failed as 'Sign out' was not found.")

if __name__ == "__main__":
    unittest.main()