import unittest
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Accept cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 2. Click on the account button and select "Register".
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found.")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link not found.")

        # 3. Fill in the registration form.
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
        except:
            self.fail("Email field not found.")

        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)
        except:
            self.fail("Password field not found.")

        try:
            repeat_password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(password)
        except:
            self.fail("Repeat Password field not found.")

        try:
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys(first_name)
        except:
            self.fail("First Name field not found.")

        try:
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys(last_name)
        except:
            self.fail("Last Name field not found.")

        # 4. Select a country and a region/state.
        try:
            country_select = Select(wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/parent::select"))
            ))
            country_select.select_by_value("CA")
        except:
            self.fail("Country select not found.")

        try:
            state_select = Select(wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/parent::select"))
            ))
            state_select.select_by_value("QC")
        except:
            self.fail("State select not found.")

        # 5. Submit the registration form.
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Register']/parent::button"))
            )
            register_button.click()
        except:
            self.fail("Register button not found.")

        # 6. Wait for redirect and confirm success.
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Registration failed. URL does not contain '/my-account'.")


if __name__ == "__main__":
    unittest.main()