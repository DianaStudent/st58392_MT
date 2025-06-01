from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the account icon/button.
        try:
            account_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found or not clickable: {e}")

        # 3. Select the "Register" option.
        try:
            register_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found or not clickable: {e}")

        # 4. Wait for the registration page to load.
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Register')]")))
        except Exception as e:
            self.fail(f"Registration page did not load correctly: {e}")

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        try:
            email_field = self.wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            password_field = self.driver.find_element(By.NAME, "password")
            repeat_password_field = self.driver.find_element(By.NAME, "repeatPassword")
            firstname_field = self.driver.find_element(By.NAME, "firstName")
            lastname_field = self.driver.find_element(By.NAME, "lastName")

            email_field.send_keys(email)
            password_field.send_keys(password)
            repeat_password_field.send_keys(password)
            firstname_field.send_keys(firstname)
            lastname_field.send_keys(lastname)

        except Exception as e:
            self.fail(f"Could not find or interact with registration form fields: {e}")

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        try:
            country_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/..")))
            country_select = Select(country_dropdown)
            country_select.select_by_index(1) #Select first country

            # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
            state_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/..")))
            state_select = Select(state_dropdown)
            state_select.select_by_index(1)

            # Click on some place to avoid country selector hide state selector.
            self.driver.find_element(By.CLASS_NAME, "login-register-wrapper").click()

        except Exception as e:
            self.fail(f"Could not select country or state: {e}")

        # 8. Submit the form.
        try:
            register_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Register')]")))
            register_button.click()
        except Exception as e:
            self.fail(f"Register button not found or not clickable: {e}")

        # 9. Wait for the page to redirect and confirm registration success.
        try:
            self.wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", self.driver.current_url, "Registration failed: Redirect to my-account was not successful.")
        except Exception as e:
            self.fail(f"Registration failed or redirect to my-account was not successful: {e}")

if __name__ == "__main__":
    unittest.main()