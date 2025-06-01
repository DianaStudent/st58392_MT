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
    URL = "http://localhost/"

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver: WebDriver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.URL)

        # 1. Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 2. Click on the account button and select "Register".
        account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()
        register_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='account-dropdown']//a[@href='/register']")
            )
        )
        register_link.click()

        # 3. Fill in the registration form.
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

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

        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)

        # 4. Select a country and a region/state.
        country_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/.."))
        )
        country = Select(country_select)
        country.select_by_value("CA")

        state_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/.."))
        )
        state = Select(state_select)
        state.select_by_value("QC")

        # 5. Submit the registration form.
        register_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Register')]"))
        )
        register_button.click()

        # 6. Wait for redirect and confirm success.
        WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        self.assertTrue("/my-account" in driver.current_url)


if __name__ == "__main__":
    unittest.main()