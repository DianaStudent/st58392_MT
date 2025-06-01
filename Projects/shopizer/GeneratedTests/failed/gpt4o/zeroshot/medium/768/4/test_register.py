from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            cookie_accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_accept_button.click()
        except:
            self.fail("Cookie accept button not found or not clickable.")

        # Click on the account button
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
        except:
            self.fail("Account button not found or not clickable.")

        # Click on the Register link
        try:
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link not found or not clickable.")

        # Fill in registration form
        try:
            email_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email_field.send_keys(f"test_{int(time.time())}@user.com")

            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys("test**11")

            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_field.send_keys("test**11")

            first_name_field = driver.find_element(By.NAME, "firstName")
            first_name_field.send_keys("Test")

            last_name_field = driver.find_element(By.NAME, "lastName")
            last_name_field.send_keys("User")

            country_dropdown = driver.find_element(By.CSS_SELECTOR, "select option[value='CA']")
            country_dropdown.click()

            state_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='stateProvince'] option[value='QC']")
            state_dropdown.click()
        except Exception as e:
            self.fail(f"An error occurred while filling the form: {e}")

        # Submit the registration form
        try:
            register_button = driver.find_element(By.CSS_SELECTOR, ".button-box button")
            register_button.click()
        except:
            self.fail("Register button not found or not clickable.")

        # Confirm redirection to my-account
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Failed to redirect or confirm URL to '/my-account'.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()