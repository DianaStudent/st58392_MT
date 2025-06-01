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
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@href='/register']")
            )
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        register_form = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h4[contains(text(), 'Register')]")
            )
        )
        self.assertIsNotNone(register_form, "Registration form not found")

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        repeat_password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "repeatPassword"))
        )
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        last_name_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )

        # Generate dynamic email
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(6))
        email = f"test_{random_string}@user.com"

        email_field.send_keys(email)
        password_field.send_keys("test**11")
        repeat_password_field.send_keys("test**11")
        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_select_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/.."))
        )
        country_select = Select(country_select_element)
        country_select.select_by_index(1)

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_select_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/.."))
        )

        # Click on the register button to ensure the state dropdown is visible
        register_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button/span[text()='Register']"))
        )
        register_button.click()

        state_select = Select(state_select_element)
        state_select.select_by_index(1)

        # 8. Submit the form.
        register_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button/span[text()='Register']"))
        )
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()