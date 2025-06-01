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
            self.fail(f"Account button not found or not clickable: {e}")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found or not clickable: {e}")

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
            self.fail(f"Email field not found: {e}")

        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)
        except Exception as e:
            self.fail(f"Password field not found: {e}")

        try:
            repeat_password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(password)
        except Exception as e:
            self.fail(f"Repeat password field not found: {e}")

        try:
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys(first_name)
        except Exception as e:
            self.fail(f"First name field not found: {e}")

        try:
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys(last_name)
        except Exception as e:
            self.fail(f"Last name field not found: {e}")

        # 4. Select a country and a region/state.
        try:
            country_select = Select(wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/.."))
            ))
            country_select.select_by_visible_text("Canada")
        except Exception as e:
            self.fail(f"Country select not found: {e}")

        try:
            state_select = Select(wait.until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/.."))
            ))
            state_select.select_by_visible_text("Quebec")
        except Exception as e:
            self.fail(f"State select not found: {e}")

        # 5. Submit the registration form.
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found or not clickable: {e}")

        # 6. Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        try:
            wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "Registration failed. Not redirected to my-account page.")
        except Exception as e:
            self.fail(f"Redirection to my-account failed: {e}")

if __name__ == "__main__":
    unittest.main()