from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import re

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        
        # Accept cookies
        try:
            accept_cookies_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()
        except:
            self.fail("Accept cookies button not found.")
        
        # Go to the register page
        try:
            account_btn = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_btn.click()

            register_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link/button not found.")

        # Fill the registration form
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            first_name_input = driver.find_element(By.NAME, "firstName")
            last_name_input = driver.find_element(By.NAME, "lastName")

            # Generate dynamic email
            email = f"test_{int(time.time())}@example.com"
            
            email_input.send_keys(email)
            password_input.send_keys("test**11")
            repeat_password_input.send_keys("test**11")
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            
            # Select country and state
            country_select = driver.find_elements(By.TAG_NAME, "select")[0]
            country_select.click()
            country_options = country_select.find_elements(By.TAG_NAME, "option")
            for option in country_options:
                if option.get_attribute("value") == "CA":
                    option.click()
                    break
            
            state_select = driver.find_elements(By.TAG_NAME, "select")[1]
            state_select.click()
            state_options = state_select.find_elements(By.TAG_NAME, "option")
            for option in state_options:
                if option.get_attribute("value") == "QC":
                    option.click()
                    break

        except:
            self.fail("Registration form inputs or selections not found.")
        
        # Submit the form
        try:
            register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            register_button.click()
        except:
            self.fail("Register button not found.")
        
        # Confirm success by checking redirected URL
        try:
            self.wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Registration success not confirmed, '/my-account' not found in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()