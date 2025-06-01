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
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def generate_dynamic_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@example.com"

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept Cookies if displayed
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            pass

        # Click on the account button and select "Register"
        account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in the registration form
        dynamic_email = self.generate_dynamic_email()

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys(dynamic_email)

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys("test**11")

        confirm_password_input = wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
        confirm_password_input.send_keys("test**11")

        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name_input.send_keys("Test")

        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        last_name_input.send_keys("User")

        # Select a country
        country_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[contains(., 'Select a country')]")))
        country_select.send_keys("Canada" + Keys.RETURN)

        # Select a region/state
        state_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[contains(., 'Select a state')]")))
        state_select.send_keys("Quebec" + Keys.RETURN)

        # Submit the registration form
        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Register']/..")))
        register_button.click()

        # Confirm success by checking the URL includes "/my-account"
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)

if __name__ == "__main__":
    unittest.main()