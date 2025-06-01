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
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
    
    def generate_random_email(self):
        return "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@user.com"
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookie acceptance button not found")
        
        # Navigate to Register page
        account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active"))
        )
        account_button.click()
        
        register_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # Fill the registration form
        try:
            email_input = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email address']"))
            )
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            first_name_input = driver.find_element(By.NAME, "firstName")
            last_name_input = driver.find_element(By.NAME, "lastName")
            country_select = driver.find_element(By.XPATH, "//select[option[text()='Select a country']]")
            state_select = driver.find_element(By.XPATH, "//select[option[text()='Select a state']]")

            random_email = self.generate_random_email()

            email_input.send_keys(random_email)
            password_input.send_keys("test**11")
            repeat_password_input.send_keys("test**11")
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            country_select.send_keys("Canada")
            state_select.send_keys("Quebec")

            register_button = driver.find_element(By.XPATH, "//button/span[text()='Register']")
            register_button.click()
        except:
            self.fail("Failed to fill registration form or register button not found")
        
        # Verify successful registration
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Registration failed or redirection to '/my-account' did not occur")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()