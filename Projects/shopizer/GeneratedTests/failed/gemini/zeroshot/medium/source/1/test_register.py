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
        self.email = f"test_{uuid.uuid4().hex}@user.com"

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

        # Click on the account button
        account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # Select "Register"
        register_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
        )
        register_link.click()

        # Fill in the registration form
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(self.email)

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys("test**11")

        repeat_password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "repeatPassword"))
        )
        repeat_password_field.send_keys("test**11")

        first_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        first_name_field.send_keys("Test")

        last_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        last_name_field.send_keys("User")

        # Select country
        country_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/../.."))
        )
        country_dropdown = Select(country_select)
        country_dropdown.select_by_value("CA")

        # Select state
        state_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../.."))
        )
        state_dropdown = Select(state_select)
        state_dropdown.select_by_value("QC")

        # Submit the registration form
        register_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Register')]"))
        )
        register_button.click()

        # Wait for redirect and confirm success
        WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        if not current_url:
            self.fail("URL is empty after registration.")
        self.assertIn("/my-account", current_url, "Registration failed: Redirect to /my-account was not successful.")


if __name__ == "__main__":
    unittest.main()