from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
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
        self.driver.maximize_window()

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
            self.fail("Account button not found")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link not found")

        # Fill registration form
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test**11"

        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            repeat_password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )

            email_field.send_keys(email)
            password_field.send_keys(password)
            repeat_password_field.send_keys(password)
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")

            country_select = Select(wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/../.."))
            ))
            country_select.select_by_visible_text("Canada")

            state_select = Select(wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../.."))
            ))
            state_select.select_by_visible_text("Quebec")

        except:
            self.fail("Could not find one or more registration form fields")

        # Submit registration form
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except:
            self.fail("Register button not found")

        # Verify successful registration
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertTrue("/my-account" in driver.current_url)
        except:
            self.fail("Registration failed. Did not redirect to /my-account")


if __name__ == "__main__":
    unittest.main()