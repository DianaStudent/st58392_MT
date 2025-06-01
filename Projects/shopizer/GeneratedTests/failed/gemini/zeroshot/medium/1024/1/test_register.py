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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
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
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 2. Click on the account button and select "Register".
        account_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        register_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # 3. Fill in the registration form.
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        email_field = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        if email_field:
            email_field.send_keys(email)
        else:
            self.fail("Email field not found")

        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        if password_field:
            password_field.send_keys(password)
        else:
            self.fail("Password field not found")

        repeat_password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "repeatPassword"))
        )
        if repeat_password_field:
            repeat_password_field.send_keys(password)
        else:
            self.fail("Repeat Password field not found")

        first_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        if first_name_field:
            first_name_field.send_keys(first_name)
        else:
            self.fail("First Name field not found")

        last_name_field = wait.until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        if last_name_field:
            last_name_field.send_keys(last_name)
        else:
            self.fail("Last Name field not found")

        # 4. Select a country and a region/state.
        country_select = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/../.."))
        )
        if country_select:
            select_country = Select(country_select)
            select_country.select_by_visible_text("Canada")
        else:
            self.fail("Country select not found")

        state_select = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../.."))
        )
        if state_select:
            select_state = Select(state_select)
            select_state.select_by_visible_text("Quebec")
        else:
            self.fail("State select not found")

        # 5. Submit the registration form.
        register_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Register']/.."))
        )
        if register_button:
            register_button.click()
        else:
            self.fail("Register button not found")

        # 6. Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url)

if __name__ == "__main__":
    unittest.main()