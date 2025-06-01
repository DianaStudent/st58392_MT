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
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver: WebDriver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"

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

        # Click on the account button and select "Register"
        account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

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

        # Select a country and a region/state
        country_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/parent::select"))
        )
        country_dropdown = Select(country_select)
        country_dropdown.select_by_value("CA")

        state_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/parent::select"))
        )
        state_dropdown = Select(state_select)
        state_dropdown.select_by_value("QC")

        # Submit the registration form
        register_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]"))
        )
        register_button.click()

        # Wait for redirect and confirm success
        WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)


if __name__ == "__main__":
    unittest.main()