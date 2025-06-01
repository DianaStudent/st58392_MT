from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')  # Assuming the website is hosted locally

    def generate_random_email(self):
        domain = "@user.com"
        username = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return username + domain

    def test_register_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail("Accept cookies button not found: " + str(e))
        
        # Navigate to Register page
        try:
            account_setting_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".same-style.account-setting button")))
            account_setting_button.click()
            
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail("Failed to navigate to register page: " + str(e))
       
        # Fill registration form
        try:
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email_input.send_keys(self.generate_random_email())

            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")

            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")

            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")

            country_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='country']")
            country_dropdown.send_keys("Canada")

            state_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='stateProvince']")
            state_dropdown.send_keys("Quebec")

            register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            register_button.click()
        except Exception as e:
            self.fail("Failed to fill registration form: " + str(e))

        # Verify registration success
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail("Registration did not redirect to '/my-account': " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()