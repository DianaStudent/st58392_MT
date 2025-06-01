from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        try:
            # Accept cookies
            accept_cookies = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()

            # Navigate to Register page
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
            
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()

            # Fill registration form
            email = self.generate_email()
            password = "test**11"

            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_input.send_keys(email)

            password_input = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(password)

            repeat_password_input = wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_input.send_keys(password)

            first_name_input = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_input.send_keys("Test")

            last_name_input = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_input.send_keys("User")

            # Select country
            country_select = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select[option='Select a country']"))
            )
            country_select.click()
            country_select.find_element(By.XPATH, "//option[@value='CA']").click()

            # Select state
            state_select = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select[option='Select a state']"))
            )
            state_select.click()
            state_select.find_element(By.XPATH, "//option[@value='QC']").click()

            # Submit the form
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span='Register']"))
            )
            register_button.click()

            # Check for successful registration
            wait.until(EC.url_contains("/my-account"))

        except Exception as e:
            self.fail(f"Test failed due to an unexpected exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()