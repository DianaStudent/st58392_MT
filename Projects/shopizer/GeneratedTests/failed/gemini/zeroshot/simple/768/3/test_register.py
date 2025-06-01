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
        service = Service(executable_path=ChromeDriverManager().install())
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
        except:
            pass

        # Go to register page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link not found")

        # Fill in registration form
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"

        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
        except:
            self.fail("Email field not found")

        try:
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)
        except:
            self.fail("Password field not found")

        try:
            repeat_password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(password)
        except:
            self.fail("Repeat password field not found")

        try:
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys("Test")
        except:
            self.fail("First name field not found")

        try:
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys("User")
        except:
            self.fail("Last name field not found")

        try:
            country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Canada']/parent::select"))
            )
            select_country = Select(country_select)
            select_country.select_by_value("CA")
        except:
            self.fail("Country select not found")

        try:
            state_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Quebec']/parent::select"))
            )
            select_state = Select(state_select)
            select_state.select_by_value("QC")
        except:
            self.fail("State select not found")

        # Submit the form
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]"))
            )
            register_button.click()
        except:
            self.fail("Register button not found")

        # Verify successful registration
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertTrue("/my-account" in driver.current_url)
        except:
            self.fail("Registration failed. Did not redirect to /my-account")

if __name__ == "__main__":
    unittest.main()