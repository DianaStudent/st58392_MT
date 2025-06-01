import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def random_email(self):
        return f"test_{random.randint(1000, 9999)}@example.com"

    def test_register(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button not found: {str(e)}")

        # Click account button
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found: {str(e)}")

        # Click register link
        try:
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found: {str(e)}")
        
        # Fill registration form
        email = self.random_email()
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_input.send_keys(email)

            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")

            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")

            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")

            # Select country
            country_select = driver.find_element(By.XPATH, "//select[@name='country']")
            country_select.send_keys(Keys.RETURN)
            country_select.send_keys(Keys.ARROW_DOWN)
            country_select.send_keys(Keys.RETURN)

            # Select state
            state_select = driver.find_element(By.XPATH, "//select[@name='state']")
            state_select.send_keys(Keys.RETURN)
            state_select.send_keys(Keys.ARROW_DOWN)
            state_select.send_keys(Keys.RETURN)
        except Exception as e:
            self.fail(f"Form filling error: {str(e)}")

        # Submit form
        try:
            register_button = driver.find_element(By.XPATH, "//button[contains(text(),'Register')]")
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found: {str(e)}")

        # Verify registration success
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Failed to navigate to /my-account: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()