import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.url = "http://localhost/"
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page (already done in setUp)

        # 2. Click on the account button and select "Register"
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
            register_link.click()
        except Exception as e:
            self.fail(f"Could not click account or register link: {e}")

        # 3. Fill in the registration form
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            repeat_password_field = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))

            email_field.send_keys(email)
            password_field.send_keys(password)
            repeat_password_field.send_keys(password)
            first_name_field.send_keys(first_name)
            last_name_field.send_keys(last_name)

        except Exception as e:
            self.fail(f"Could not fill registration form: {e}")

        # 4. Select a country and a region/state
        try:
            country_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/parent::select")))
            country_select.click()
            country_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[@value='CA']")))
            country_option.click()

            state_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/parent::select")))
            state_select.click()
            state_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[@value='QC']")))
            state_option.click()

        except Exception as e:
            self.fail(f"Could not select country or state: {e}")

        # 5. Submit the registration form
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Register')]")))
            register_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # 6. Wait for redirect and confirm success
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Registration failed or redirect to /my-account did not happen: {e}")

if __name__ == "__main__":
    unittest.main()