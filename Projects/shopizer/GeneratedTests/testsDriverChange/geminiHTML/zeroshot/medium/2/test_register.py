import unittest
import random
import string
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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the account button and select "Register".
        try:
            account_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            register_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Failed to click account or register link: {e}")

        # 3. Fill in the registration form.
        try:
            # Generate random email
            email = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@user.com"

            email_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)

            password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys("test**11")

            repeat_password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys("test**11")

            first_name_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys("Test")

            last_name_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys("User")

        except Exception as e:
            self.fail(f"Failed to fill in registration form: {e}")

        # 4. Select a country and a region/state.
        try:
            country_select = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/.."))
            )
            select_country = Select(country_select)
            select_country.select_by_value("CA")

            state_select = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/.."))
            )
            select_state = Select(state_select)
            select_state.select_by_value("QC")
        except Exception as e:
            self.fail(f"Failed to select country and state: {e}")

        # 5. Submit the registration form.
        try:
            register_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span='Register']"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to submit registration form: {e}")

        # 6. Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        try:
            self.wait.until(EC.url_contains("/my-account"))
            current_url = self.driver.current_url
            self.assertIn("/my-account", current_url, "Registration failed. URL does not contain '/my-account'")
        except Exception as e:
            self.fail(f"Registration failed or redirect to my-account was not successful: {e}")


if __name__ == "__main__":
    unittest.main()