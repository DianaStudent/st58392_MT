from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random
import string

class TestUserRegistration(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()
    
    def generate_random_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
    
    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except Exception:
            self.fail("Cookie acceptance button not found")
        
        # Navigate to Register page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception:
            self.fail("Navigation to register page failed")

        # Fill registration form
        try:
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            first_name_input = driver.find_element(By.NAME, "firstName")
            last_name_input = driver.find_element(By.NAME, "lastName")
            country_select = driver.find_element(By.XPATH, "//select[option[text()='Select a country']]")
            state_select = driver.find_element(By.XPATH, "//select[option[text()='Select a state']]")
            
            email_input.send_keys(self.generate_random_email())
            password_input.send_keys("test**11")
            repeat_password_input.send_keys("test**11")
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            country_select.send_keys(Keys.DOWN, Keys.ENTER) # Select first country
            state_select.send_keys(Keys.DOWN, Keys.ENTER) # Select first state
        except Exception:
            self.fail("Filling registration form failed")

        # Submit registration form
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
            submit_button.click()
        except Exception:
            self.fail("Submit button not found")

        # Confirm successful registration by checking URL
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception:
            self.fail("Registration did not lead to /my-account page")
        
if __name__ == "__main__":
    unittest.main()