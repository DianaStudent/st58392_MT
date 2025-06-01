from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Go to register page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
            register_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to register page: {e}")

        # Fill in registration form
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        try:
            email_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
            repeat_password_field = wait.until(EC.element_to_be_clickable((By.NAME, "repeatPassword")))
            first_name_field = wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
            last_name_field = wait.until(EC.element_to_be_clickable((By.NAME, "lastName")))
            country_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/..")))
            state_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/..")))

            email_field.send_keys(email)
            password_field.send_keys(password)
            repeat_password_field.send_keys(password)
            first_name_field.send_keys(first_name)
            last_name_field.send_keys(last_name)

            country_dropdown = Select(country_select)
            country_dropdown.select_by_value("CA")

            state_dropdown = Select(state_select)
            state_dropdown.select_by_value("QC")

        except Exception as e:
            self.fail(f"Could not find or fill form fields: {e}")

        # Submit registration form
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]")))
            register_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # Verify successful registration
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except Exception as e:
            self.fail(f"Registration failed or redirect to /my-account did not happen: {e}")

if __name__ == "__main__":
    unittest.main()