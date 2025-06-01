import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button: WebElement = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except TimeoutException:
            self.fail("Cookie accept button not found")

        # Go to register page
        try:
            account_setting_button: WebElement = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_setting_button.click()
        except TimeoutException:
            self.fail("Account settings button not found")

        try:
            register_link: WebElement = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
            )
            register_link.click()
        except TimeoutException:
            self.fail("Register link not found")

        # Fill registration form
        try:
            email_field: WebElement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(self.email)
        except TimeoutException:
            self.fail("Email field not found")

        try:
            password_field: WebElement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(self.password)
        except TimeoutException:
            self.fail("Password field not found")

        try:
            repeat_password_field: WebElement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "repeatPassword"))
            )
            repeat_password_field.send_keys(self.password)
        except TimeoutException:
            self.fail("Repeat Password field not found")

        try:
            first_name_field: WebElement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys("Test")
        except TimeoutException:
            self.fail("First Name field not found")

        try:
            last_name_field: WebElement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys("User")
        except TimeoutException:
            self.fail("Last Name field not found")

        try:
            country_select: WebElement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Canada']"))
            )
            country_select.click()
        except TimeoutException:
            self.fail("Country select not found")

        try:
            state_select: WebElement = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Quebec']"))
            )
            state_select.click()
        except TimeoutException:
            self.fail("State select not found")

        # Submit registration form
        try:
            register_button: WebElement = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Register')]"))
            )
            register_button.click()
        except TimeoutException:
            self.fail("Register button not found")

        # Verify successful registration
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except TimeoutException:
            self.fail("Registration failed, URL does not contain '/my-account'")


if __name__ == "__main__":
    unittest.main()