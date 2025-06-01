from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            cookies_button.click()
        except:
            self.fail("Cookies acceptance button not found or clicked")

        # Navigate to Register page
        account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in the registration form
        email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@example.com"

        try:
            email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            email_field.send_keys(email)

            password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            password_field.send_keys("test**11")

            repeat_password_field = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            repeat_password_field.send_keys("test**11")

            first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            first_name_field.send_keys("Test")

            last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            last_name_field.send_keys("User")

            country_select = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[option='Select a country']")))
            country_select.send_keys("Canada")

            state_select = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[option='Select a state']")))
            state_select.send_keys("Quebec")
        except:
            self.fail("Failed to fill one or more fields in the registration form.")

        # Submit the registration form
        register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Register']")))
        register_button.click()

        # Check success by URL redirection
        try:
            wait.until(lambda driver: "/my-account" in driver.current_url)
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Redirection to '/my-account' did not occur.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()