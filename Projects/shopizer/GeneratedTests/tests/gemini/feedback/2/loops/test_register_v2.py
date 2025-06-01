import unittest
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

        # Accept cookies if the banner is present
        try:
            cookie_button_locator = (By.ID, "rcc-confirm-button")
            cookie_button = self.wait.until(EC.presence_of_element_located(cookie_button_locator))
            cookie_button.click()
        except:
            pass

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the account icon/button.
        account_button_locator = (By.CLASS_NAME, "account-setting-active")
        account_button = self.wait.until(EC.presence_of_element_located(account_button_locator))
        account_button.click()

        # 3. Select the "Register" option.
        register_link_locator = (By.LINK_TEXT, "Register")
        register_link = self.wait.until(EC.presence_of_element_located(register_link_locator))
        register_link.click()

        # 4. Wait for the registration page to load.
        register_form_locator = (By.NAME, "email")
        self.wait.until(EC.presence_of_element_located(register_form_locator))

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = "test_" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6)) + "@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field_locator = (By.NAME, "email")
        email_field = self.wait.until(EC.presence_of_element_located(email_field_locator))
        email_field.send_keys(email)

        password_field_locator = (By.NAME, "password")
        password_field = self.wait.until(EC.presence_of_element_located(password_field_locator))
        password_field.send_keys(password)

        repeat_password_field_locator = (By.NAME, "repeatPassword")
        repeat_password_field = self.wait.until(EC.presence_of_element_located(repeat_password_field_locator))
        repeat_password_field.send_keys(password)

        firstname_field_locator = (By.NAME, "firstName")
        firstname_field = self.wait.until(EC.presence_of_element_located(firstname_field_locator))
        firstname_field.send_keys(firstname)

        lastname_field_locator = (By.NAME, "lastName")
        lastname_field = self.wait.until(EC.presence_of_element_located(lastname_field_locator))
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown_locator = (By.XPATH, "//select/option[text()='Select a country']/../option[2]")
        country_dropdown = self.wait.until(EC.presence_of_element_located(country_dropdown_locator))
        country_dropdown.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown_locator = (By.XPATH, "//select/option[text()='Select a state']/../option[2]")
        state_dropdown = self.wait.until(EC.presence_of_element_located(state_dropdown_locator))
        state_dropdown.click()

        # 8. Submit the form.
        register_button_locator = (By.XPATH, "//button[contains(.,'Register')]")
        register_button = self.wait.until(EC.presence_of_element_located(register_button_locator))
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()