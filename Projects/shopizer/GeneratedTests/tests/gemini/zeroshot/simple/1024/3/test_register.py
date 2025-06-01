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
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Go to register page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to register page: {e}")

        # Fill registration form
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_field.send_keys(email)

            password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password_field.send_keys(password)

            repeat_password_field = wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
            repeat_password_field.send_keys(password)

            first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            first_name_field.send_keys(first_name)

            last_name_field = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
            last_name_field.send_keys(last_name)

            country_select = Select(wait.until(EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/../.."))))
            country_select.select_by_visible_text("Canada")

            state_select = Select(wait.until(EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/../.."))))
            state_select.select_by_visible_text("Quebec")
        except Exception as e:
            self.fail(f"Could not fill registration form: {e}")

        # Submit registration form
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span='Register']")))
            register_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # Verify successful registration
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Registration failed: {e}")

if __name__ == "__main__":
    unittest.main()