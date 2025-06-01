from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Go to register page
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Could not find account settings button")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Could not find register link")

        # Fill registration form
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
        except:
            self.fail("Could not find email field")

        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)
        except:
            self.fail("Could not find password field")

        try:
            repeat_password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(password)
        except:
            self.fail("Could not find repeat password field")

        try:
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys(first_name)
        except:
            self.fail("Could not find first name field")

        try:
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys(last_name)
        except:
            self.fail("Could not find last name field")

        try:
            country_select = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/../.."))
            )
            select_country = Select(country_select)
            select_country.select_by_value("CA")
        except:
            self.fail("Could not find country select")

        try:
            state_select = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../.."))
            )
            select_state = Select(state_select)
            select_state.select_by_value("QC")
        except:
            self.fail("Could not find state select")

        # Submit the form
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except:
            self.fail("Could not find register button")

        # Check for success
        wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)


if __name__ == "__main__":
    unittest.main()