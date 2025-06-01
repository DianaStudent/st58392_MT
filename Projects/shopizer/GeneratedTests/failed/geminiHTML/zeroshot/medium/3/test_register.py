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
from selenium.webdriver.support.ui import Select

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.email = f"test_{uuid.uuid4().hex}@user.com"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        # 1. Open the home page. (Done in setUp)

        # 2. Click on the account button and select "Register".
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found or not clickable: {e}")

        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found or not clickable: {e}")

        # 3. Fill in the registration form.
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(self.email)
        except Exception as e:
            self.fail(f"Email field not found: {e}")

        try:
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys("test**11")
        except Exception as e:
            self.fail(f"Password field not found: {e}")

        try:
            repeat_password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys("test**11")
        except Exception as e:
            self.fail(f"Repeat Password field not found: {e}")

        try:
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys("Test")
        except Exception as e:
            self.fail(f"First Name field not found: {e}")

        try:
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys("User")
        except Exception as e:
            self.fail(f"Last Name field not found: {e}")

        # 4. Select a country and a region/state.
        try:
            country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/parent::select"))
            )
            country_select_obj = Select(country_select)
            country_select_obj.select_by_value("CA")
        except Exception as e:
            self.fail(f"Country select not found or Canada option not available: {e}")

        try:
            state_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/parent::select"))
            )
            state_select_obj = Select(state_select)
            state_select_obj.select_by_value("QC")
        except Exception as e:
            self.fail(f"State select not found or Quebec option not available: {e}")

        # 5. Submit the registration form.
        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found or not clickable: {e}")

        # 6. Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "Registration failed. Redirect URL does not contain '/my-account'.")
        except Exception as e:
            self.fail(f"Redirection to my-account failed or timed out: {e}")

if __name__ == "__main__":
    unittest.main()