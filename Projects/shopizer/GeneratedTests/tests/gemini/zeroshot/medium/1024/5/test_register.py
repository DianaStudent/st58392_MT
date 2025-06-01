import unittest
import time
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Accept cookies
        try:
            cookie_button = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 2. Click on the account button and select "Register"
        account_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        register_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))
        )
        register_link.click()

        # 3. Fill in the registration form
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        email_field = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(email)

        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)

        repeat_password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "repeatPassword"))
        )
        repeat_password_field.send_keys(password)

        first_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        first_name_field.send_keys(first_name)

        last_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        last_name_field.send_keys(last_name)

        # 4. Select a country and a region/state
        country_select = wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/../.."))
        )
        country_dropdown = Select(country_select)
        country_dropdown.select_by_value("CA")

        state_select = wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/../.."))
        )
        state_dropdown = Select(state_select)
        state_dropdown.select_by_value("QC")

        # 5. Submit the registration form
        register_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[span='Register']"))
        )
        register_button.click()

        # 6. Wait for redirect and confirm success
        wait.until(EC.url_contains("/my-account"))
        self.assertTrue("/my-account" in driver.current_url)

if __name__ == "__main__":
    unittest.main()