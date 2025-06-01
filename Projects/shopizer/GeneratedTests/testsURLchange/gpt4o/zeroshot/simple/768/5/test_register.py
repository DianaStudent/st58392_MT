from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import uuid

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found: {e}")

        # Navigate to registration page
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found: {e}")

        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found: {e}")

        # Fill registration form
        email = f"test_{uuid.uuid4().hex[:6]}@example.com"

        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_input.send_keys(email)

            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")

            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")

            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")

            country_select = driver.find_element(By.XPATH, "//select[option[@value='CA']]")
            country_select.click()

            state_select = driver.find_element(By.XPATH, "//select[option[@value='QC']]")
            state_select.click()

            register_button = driver.find_element(By.XPATH, "//button/span[contains(text(),'Register')]/..")
            register_button.click()

        except Exception as e:
            self.fail(f"Form element not found or interaction failed: {e}")

        # Confirm registration success
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Registration did not redirect to /my-account: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()