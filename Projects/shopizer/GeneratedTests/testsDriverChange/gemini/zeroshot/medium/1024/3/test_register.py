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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the account button and select "Register".
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Could not find or click account button: {e}")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click register link: {e}")

        # 3. Fill in the registration form.
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
        except Exception as e:
            self.fail(f"Could not find or enter email: {e}")

        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)
        except Exception as e:
            self.fail(f"Could not find or enter password: {e}")

        try:
            repeat_password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(password)
        except Exception as e:
            self.fail(f"Could not find or enter repeat password: {e}")

        try:
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys(first_name)
        except Exception as e:
            self.fail(f"Could not find or enter first name: {e}")

        try:
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys(last_name)
        except Exception as e:
            self.fail(f"Could not find or enter last name: {e}")

        # 4. Select a country and a region/state.
        try:
            country_select = Select(wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "select"))
            ))
            country_select.select_by_value("CA")
        except Exception as e:
            self.fail(f"Could not find or select country: {e}")

        try:
            state_select = Select(wait.until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "select"))[1]
            ))
            state_select.select_by_value("QC")
        except Exception as e:
            self.fail(f"Could not find or select state: {e}")

        # 5. Submit the registration form.
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.TAG_NAME, "button"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Could not find or click register button: {e}")

        # 6. Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertTrue("/my-account" in driver.current_url, "Registration failed. Redirect URL does not contain '/my-account'.")
        except Exception as e:
            self.fail(f"Registration failed or redirect to /my-account did not happen: {e}")

if __name__ == "__main__":
    unittest.main()