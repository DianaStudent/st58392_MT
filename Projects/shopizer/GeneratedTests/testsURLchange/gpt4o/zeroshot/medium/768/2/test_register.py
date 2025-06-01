import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        
    def generate_email(self):
        return "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"

    def test_registration(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        # Accept cookies
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Accept cookies button not found or not clickable")

        # Navigate to Register page
        try:
            account_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".same-style.account-setting"))
            )
            account_button.click()

            register_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_button.click()
        except:
            self.fail("Navigation to Register page failed")

        # Fill the registration form
        try:
            email_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_field = driver.find_element(By.NAME, "password")
            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            first_name_field = driver.find_element(By.NAME, "firstName")
            last_name_field = driver.find_element(By.NAME, "lastName")

            email = self.generate_email()
            email_field.send_keys(email)
            password_field.send_keys("test**11")
            repeat_password_field.send_keys("test**11")
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")

            country_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='country']")
            country_dropdown.send_keys("Canada")
            
            state_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='state']")
            state_dropdown.send_keys("Quebec")

            register_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            register_submit.click()
        except:
            self.fail("Filling registration form failed")

        # Confirm successful registration
        try:
            self.wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "Registration success confirmation failed")
        except:
            self.fail("Redirection to /my-account failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()