import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.url = "http://localhost/"
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        self.password = "test**11"
        self.firstName = "Test"
        self.lastName = "User"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 2. Click on the account button and select "Register".
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found or not clickable.")

        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
            )
            register_link.click()
        except:
            self.fail("Register link not found or not clickable.")

        # 3. Fill in the registration form.
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(self.email)
        except:
            self.fail("Email field not found.")

        try:
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(self.password)
        except:
            self.fail("Password field not found.")

        try:
            repeat_password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(self.password)
        except:
            self.fail("Repeat Password field not found.")

        try:
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys(self.firstName)
        except:
            self.fail("First Name field not found.")

        try:
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys(self.lastName)
        except:
            self.fail("Last Name field not found.")

        # 4. Select a country and a region/state.
        try:
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Canada']/parent::select"))
            )
            select_country = Select(country_select)
            select_country.select_by_visible_text("Canada")
        except:
            self.fail("Country select not found or Canada option missing.")

        try:
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Quebec']/parent::select"))
            )
            select_state = Select(state_select)
            select_state.select_by_visible_text("Quebec")
        except:
            self.fail("State select not found or Quebec option missing.")

        # 5. Submit the registration form.
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except:
            self.fail("Register button not found or not clickable.")

        # 6. Wait for redirect and confirm success.
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertTrue("/my-account" in driver.current_url, "Registration failed. Not redirected to my-account page.")
        except:
            self.fail("Registration failed or redirect timed out.")

if __name__ == "__main__":
    unittest.main()