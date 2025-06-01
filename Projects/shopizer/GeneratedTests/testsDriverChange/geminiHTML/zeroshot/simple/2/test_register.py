import unittest
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except NoSuchElementException:
            print("Cookie button not found, continuing...")

        # Go to register page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except NoSuchElementException:
            self.fail("Could not find account or register link.")

        # Fill registration form
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            repeat_password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/parent::select"))
            )
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/parent::select"))
            )
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]"))
            )

            email_field.send_keys(email)
            password_field.send_keys(password)
            repeat_password_field.send_keys(password)
            first_name_field.send_keys(first_name)
            last_name_field.send_keys(last_name)

            # Select Canada
            country_select.click()
            canada_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Canada']"))
            )
            canada_option.click()

            # Select Quebec
            state_select.click()
            quebec_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Quebec']"))
            )
            quebec_option.click()

            register_button.click()

        except NoSuchElementException:
            self.fail("Could not find registration form elements.")

        # Check for successful registration
        WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)


if __name__ == "__main__":
    unittest.main()