from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/"
    
    def random_email(self):
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"test_{suffix}@user.com"

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # Accept cookies
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie consent acceptance failed: {str(e)}")

        # Click account icon/button
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Unable to locate account icon/button: {str(e)}")

        # Select the "Register" option
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Unable to locate register link: {str(e)}")

        # Wait for the registration page to load and fill out the fields
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            first_name_input = driver.find_element(By.NAME, "firstName")
            last_name_input = driver.find_element(By.NAME, "lastName")

            email = self.random_email()
            email_input.send_keys(email)
            password_input.send_keys("test**11")
            repeat_password_input.send_keys("test**11")
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
        except Exception as e:
            self.fail(f"Failed to fill registration form: {str(e)}")

        # Select the first country from the dropdown and wait for region/state dropdown
        try:
            country_dropdown = driver.find_elements(By.TAG_NAME, "select")[0]
            country_dropdown.click()
            country_dropdown.find_elements(By.TAG_NAME, "option")[1].click()
        except Exception as e:
            self.fail(f"Country selection failed: {str(e)}")

        # Select the first state after selecting the country
        try:
            state_dropdown = driver.find_elements(By.TAG_NAME, "select")[1]
            state_dropdown.click()
            state_dropdown.find_elements(By.TAG_NAME, "option")[1].click()
        except Exception as e:
            self.fail(f"State selection failed: {str(e)}")

        # Submit the form
        try:
            submit_button = driver.find_element(By.XPATH, "//button[text()='Register']")
            submit_button.click()
        except Exception as e:
            self.fail(f"Form submission failed: {str(e)}")

        # Confirm registration success by checking for "/my-account" in URL
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
        except Exception as e:
            self.fail(f"Registration failed, redirect not to '/my-account': {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()