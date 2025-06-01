import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_register_user(self):
        driver = self.driver

        # Wait and accept cookies
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'rcc-confirm-button'))
            ).click()
        except Exception as e:
            self.fail(f"Cookie consent button not found: {str(e)}")

        # Click on the account icon/button
        try:
            account_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'account-setting-active'))
            )
            account_icon.click()
        except Exception as e:
            self.fail(f"Account setting icon/button not found: {str(e)}")

        # Click on "Register" option
        try:
            register_link = driver.find_element(By.LINK_TEXT, 'Register')
            register_link.click()
        except Exception as e:
            self.fail(f"Register link was not found/click: {str(e)}")

        # Wait for registration form to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
        except Exception as e:
            self.fail(f"Registration form did not load: {str(e)}")

        # Fill out registration details
        email = f"test_{random.randint(100000, 999999)}@user.com"

        # Enter email
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys(email)

        # Enter password and repeat password
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys("test**11")

        repeat_password_input = driver.find_element(By.NAME, 'repeatPassword')
        repeat_password_input.send_keys("test**11")

        # Enter first name and last name
        first_name_input = driver.find_element(By.NAME, 'firstName')
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.NAME, 'lastName')
        last_name_input.send_keys("User")

        # Select country
        country_dropdown = driver.find_element(By.XPATH, "//select[@name='']/option[2]")
        country_dropdown.click()

        # Select the state (avoid hardcoded sleep; using ActionChains to ensure dropdown switches)
        ActionChains(driver).move_by_offset(0, 0).click().perform()
        state_dropdown = driver.find_element(By.XPATH, "//select[@name='']/option[2]")
        state_dropdown.click()

        # Submit form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Verify the registration success
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Registration success redirection failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()