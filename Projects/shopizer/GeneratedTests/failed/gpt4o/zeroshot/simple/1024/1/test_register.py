from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail("Failed to find and click accept cookies button: " + str(e))

        # Navigate to Register page
        try:
            account_settings_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_settings_button.click()

            register_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail("Failed to navigate to registration page: " + str(e))

        # Fill registration form
        try:
            email = f"test_{''.join(random.choice(string.ascii_letters) for _ in range(6))}@user.com"
            
            email_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)

            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys("test**11")

            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_field.send_keys("test**11")

            first_name_field = driver.find_element(By.NAME, "firstName")
            first_name_field.send_keys("Test")

            last_name_field = driver.find_element(By.NAME, "lastName")
            last_name_field.send_keys("User")

            # Select country
            country_select = driver.find_element(By.XPATH, '//select[option="Select a country"]')
            country_select.click()
            country_option = driver.find_element(By.XPATH, '//option[@value="CA"]')
            country_option.click()

            # Select state
            state_select = driver.find_element(By.XPATH, '//select[option="Select a state"]')
            state_select.click()
            state_option = driver.find_element(By.XPATH, '//option[@value="QC"]')
            state_option.click()

            register_button = driver.find_element(By.XPATH, '//button/span[text()="Register"]')
            register_button.click()
        except Exception as e:
            self.fail("Failed to fill or submit registration form: " + str(e))

        # Confirm registration success
        try:
            self.wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail("Registration did not lead to my-account page: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()