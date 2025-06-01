import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def generate_email(self):
        # Generate a random email address
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return f"test_{random_string}@user.com"

    def test_register_user(self):
        driver = self.driver
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        # Open the home page
        driver.get("http://localhost/")
        
        # Accept cookies if present
        try:
            accept_cookies_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_btn.click()
        except:
            pass

        # Click on the account button and select "Register"
        account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in the registration form
        email = self.generate_email()
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys(email)

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys(password)

        repeat_password_input = wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
        repeat_password_input.send_keys(password)

        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name_input.send_keys(first_name)

        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        last_name_input.send_keys(last_name)

        # Select a country and region/state
        country_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='Select a country']]")))
        country_select.click()
        country_option = wait.until(EC.presence_of_element_located((By.XPATH, "//select/option[@value='CA']")))
        country_option.click()

        state_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='Select a state']]")))
        state_select.click()
        state_option = wait.until(EC.presence_of_element_located((By.XPATH, "//select/option[@value='QC']")))
        state_option.click()

        # Submit the registration form
        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]")))
        register_button.click()

        # Wait for redirect and confirm success
        time.sleep(5)  # Static wait to allow redirect
        current_url = driver.current_url

        if '/my-account' not in current_url:
            self.fail("Failed to redirect to My Account page after registration.")

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()