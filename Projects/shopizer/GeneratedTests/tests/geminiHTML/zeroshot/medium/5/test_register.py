import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class RegistrationTest(unittest.TestCase):
    EMAIL_PREFIX = "test_"
    EMAIL_SUFFIX = "@user.com"
    PASSWORD = "test**11"
    FIRST_NAME = "Test"
    LAST_NAME = "User"
    BASE_URL = "http://localhost/"
    REGISTER_URL = BASE_URL + "register"
    MY_ACCOUNT_URL = BASE_URL + "my-account"

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver: WebDriver = webdriver.Chrome(service=service)
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.email = self.EMAIL_PREFIX + str(uuid.uuid4()).split("-")[0] + self.EMAIL_SUFFIX

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except Exception as e:
            print("Cookie button not found or not clickable.")

        # Click on the account button and select "Register"
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not click on account or register link: {e}")

        # Fill in the registration form
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

            email_field.send_keys(self.email)
            password_field.send_keys(self.PASSWORD)
            repeat_password_field.send_keys(self.PASSWORD)
            first_name_field.send_keys(self.FIRST_NAME)
            last_name_field.send_keys(self.LAST_NAME)

        except Exception as e:
            self.fail(f"Could not fill in registration form: {e}")

        # Select a country and a region/state
        try:
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/.."))
            )
            country_select.click()
            canada_option = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[@value='CA']"))
            )
            canada_option.click()

            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/.."))
            )
            state_select.click()
            quebec_option = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[@value='QC']"))
            )
            quebec_option.click()

        except Exception as e:
            self.fail(f"Could not select country or state: {e}")

        # Submit the registration form
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # Wait for redirect and confirm success
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Registration failed or redirect did not happen: {e}")


if __name__ == "__main__":
    unittest.main()