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

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the account button and select "Register".
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Failed to click account button: {e}")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Failed to click register link: {e}")

        # 3. Fill in the registration form.
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
        except Exception as e:
            self.fail(f"Failed to enter email: {e}")

        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)
        except Exception as e:
            self.fail(f"Failed to enter password: {e}")

        try:
            repeat_password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(password)
        except Exception as e:
            self.fail(f"Failed to enter repeat password: {e}")

        try:
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys(first_name)
        except Exception as e:
            self.fail(f"Failed to enter first name: {e}")

        try:
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys(last_name)
        except Exception as e:
            self.fail(f"Failed to enter last name: {e}")

        # 4. Select a country and a region/state.
        try:
            country_select = Select(wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/../.."))
            ))
            country_select.select_by_value("CA")
        except Exception as e:
            self.fail(f"Failed to select country: {e}")

        try:
            state_select = Select(wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/../.."))
            ))
            state_select.select_by_value("QC")
        except Exception as e:
            self.fail(f"Failed to select state: {e}")

        # 5. Submit the registration form.
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span='Register']"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Failed to click register button: {e}")

        # 6. Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Registration failed or redirect to /my-account did not happen: {e}")

if __name__ == "__main__":
    unittest.main()