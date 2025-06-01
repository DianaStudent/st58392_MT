import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Click on the account icon/button.
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        register_form = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//form"))
        )

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email_prefix = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = f"{email_prefix}@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(email)

        password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)

        repeat_password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "repeatPassword"))
        )
        repeat_password_field.send_keys(password)

        firstname_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        firstname_field.send_keys(firstname)

        lastname_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/.."))
        )
        country_select = Select(country_dropdown)
        country_select.select_by_index(1)

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/.."))
        )

        # Click on the firstname field to ensure the state dropdown is visible
        firstname_field.click()

        state_select = Select(state_dropdown)
        state_select.select_by_index(1)

        # 8. Submit the form.
        submit_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Register']]"))
        )
        submit_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()