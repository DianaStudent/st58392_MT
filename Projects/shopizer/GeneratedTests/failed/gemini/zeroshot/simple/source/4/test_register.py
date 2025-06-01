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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.url = "http://localhost/"
        self.email = f"test_{uuid.uuid4().hex}@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        driver.get(self.url)

        # Accept cookies
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()
        except:
            pass

        # Go to register page
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
            ).click()
        except:
            self.fail("Register link not found")

        # Fill registration form
        try:
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

            email_field.send_keys(self.email)
            password_field.send_keys(self.password)
            repeat_password_field.send_keys(self.password)
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")

            country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/../option[@value='CA']"))
            )
            country_select.click()

            state_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/../option[@value='QC']"))
            )
            state_select.click()

            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Register')]"))
            )
            register_button.click()

        except Exception as e:
            self.fail(f"Failed to fill registration form: {e}")

        # Check for success
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Registration failed: Redirect to /my-account was not successful")


if __name__ == "__main__":
    unittest.main()