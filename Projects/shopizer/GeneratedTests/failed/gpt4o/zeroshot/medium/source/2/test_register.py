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

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def generate_email(self):
        domain = "@example.com"
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return random_string + domain

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found or could not be clicked")

        # Click account button and select "Register"
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
        except:
            self.fail("Account button not found or could not be clicked")

        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link not found or could not be clicked")

        # Fill registration form
        email = self.generate_email()
        user_details = {
            "email": email,
            "password": "test**11",
            "first_name": "Test",
            "last_name": "User"
        }

        try:
            email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            email_field.send_keys(user_details["email"])

            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(user_details["password"])

            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_field.send_keys(user_details["password"])

            first_name_field = driver.find_element(By.NAME, "firstName")
            first_name_field.send_keys(user_details["first_name"])

            last_name_field = driver.find_element(By.NAME, "lastName")
            last_name_field.send_keys(user_details["last_name"])

            # Select a country (Canada) and a region/state (Quebec)
            country_select = driver.find_element(By.XPATH, "//select[1]")
            country_select.click()
            country_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[1]/option[@value='CA']")))
            country_option.click()

            state_select = driver.find_element(By.XPATH, "//select[2]")
            state_select.click()
            state_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[2]/option[@value='QC']")))
            state_option.click()

            # Submit the registration form
            register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span='Register']")))
            register_button.click()

            # Verify redirection to "/my-account"
            wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url)

        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()