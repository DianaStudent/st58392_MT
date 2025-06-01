from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string


class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")  # Assuming this is the correct URL

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found: {str(e)}")

        # Navigate to Register
        try:
            account_setting_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_setting_button.click()
            register_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Register']"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Navigation to register page failed: {str(e)}")

        # Fill registration form
        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            first_name_input = driver.find_element(By.NAME, "firstName")
            last_name_input = driver.find_element(By.NAME, "lastName")

            # Generate a random email
            email = f"test_{self.random_string()}@user.com"
            email_input.send_keys(email)
            password_input.send_keys("test**11")
            repeat_password_input.send_keys("test**11")
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")

            # Select country and state
            country_select = driver.find_elements(By.TAG_NAME, "select")[0]
            state_select = driver.find_elements(By.TAG_NAME, "select")[1]
            country_select.send_keys("Canada")
            state_select.send_keys("Quebec")

            # Submit the registration form
            register_button = driver.find_element(By.XPATH, "//button[@type='submit']/span[text()='Register']")
            register_button.click()
        except Exception as e:
            self.fail(f"Filling registration form failed: {str(e)}")

        # Confirm success by checking URL contains "/my-account"
        try:
            wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url)
        except Exception as e:
            self.fail(f"Registration success check failed: {str(e)}")

    def random_string(self, length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()