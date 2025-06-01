from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
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
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Go to register page
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Could not find account button")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Could not find register link")

        # Fill registration form
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"

        try:
            email_field = wait.until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            password_field = wait.until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            repeat_password_field = wait.until(
                EC.visibility_of_element_located((By.NAME, "repeatPassword"))
            )
            first_name_field = wait.until(
                EC.visibility_of_element_located((By.NAME, "firstName"))
            )
            last_name_field = wait.until(
                EC.visibility_of_element_located((By.NAME, "lastName"))
            )

            email_field.send_keys(email)
            password_field.send_keys(password)
            repeat_password_field.send_keys(password)
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")

            country_select = Select(wait.until(
                EC.visibility_of_element_located((By.XPATH, "//select[1]"))
            ))
            country_select.select_by_value("CA")

            state_select = Select(wait.until(
                EC.visibility_of_element_located((By.XPATH, "//select[2]"))
            ))
            state_select.select_by_value("QC")

        except:
            self.fail("Could not find registration form fields")

        # Submit registration form
        try:
            register_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]"))
            )
            register_button.click()
        except:
            self.fail("Could not find register button")

        # Check for success
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Registration failed, URL does not contain /my-account")


if __name__ == "__main__":
    unittest.main()