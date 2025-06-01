import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver

        # Accept cookies
        self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button"))).click()

        # Click on the account icon/button
        try:
            account_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except TimeoutException:
            self.fail("Account button not clickable.")

        # Select the "Register" option
        try:
            register_option = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_option.click()
        except TimeoutException:
            self.fail("Register option not clickable.")

        # Wait for the registration page to load
        if not self.wait.until(EC.presence_of_element_located((By.NAME, "email"))):
            self.fail("Email input box not found.")

        # Fill in registration form
        email = "test_{}@user.com".format(int(time.time()))
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Select country
        try:
            country_dropdown = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//select[option[@value='CA']]"))
            )
            country_dropdown.click()
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//option[@value='CA']"))
            ).click()
        except TimeoutException:
            self.fail("Country dropdown not found or not clickable.")

        # Select state
        try:
            state_dropdown = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//select[option[@value='QC']]"))
            )
            state_dropdown.click()
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//option[@value='QC']"))
            ).click()
        except TimeoutException:
            self.fail("State dropdown not found or not clickable.")

        # Submit the form
        try:
            register_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Register']]"))
            )
            register_button.click()
        except TimeoutException:
            self.fail("Register button not clickable.")

        # Confirm registration success
        if not self.wait.until(EC.url_contains("/my-account")):
            self.fail("Registration did not redirect to /my-account.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()