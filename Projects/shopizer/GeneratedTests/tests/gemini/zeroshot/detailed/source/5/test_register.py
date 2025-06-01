import unittest
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
        self.wait = WebDriverWait(self.driver, 20)

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
        email_field_locator = (By.NAME, "email")
        self.wait.until(EC.presence_of_element_located(email_field_locator))

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field = self.driver.find_element(*email_field_locator)
        password_field = self.driver.find_element(By.NAME, "password")
        repeat_password_field = self.driver.find_element(By.NAME, "repeatPassword")
        firstname_field = self.driver.find_element(By.NAME, "firstName")
        lastname_field = self.driver.find_element(By.NAME, "lastName")

        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown_locator = (By.XPATH, "//select/option[text()='Select a country']/..")
        country_dropdown = self.wait.until(EC.presence_of_element_located(country_dropdown_locator))
        country_dropdown.click()

        canada_option_locator = (By.XPATH, "//select/option[text()='Canada']")
        canada_option = self.wait.until(EC.presence_of_element_located(canada_option_locator))
        canada_option.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown_locator = (By.XPATH, "//select/option[text()='Select a state']/..")
        state_dropdown = self.wait.until(EC.presence_of_element_located(state_dropdown_locator))

        # Click outside dropdown to ensure it closes.
        ActionChains(self.driver).move_to_element(lastname_field).click().perform()

        state_dropdown.click()

        quebec_option_locator = (By.XPATH, "//select/option[text()='Quebec']")
        quebec_option = self.wait.until(EC.presence_of_element_located(quebec_option_locator))
        quebec_option.click()

        # 8. Submit the form.
        register_button_locator = (By.XPATH, "//button/span[text()='Register']/..")
        register_button = self.wait.until(EC.presence_of_element_located(register_button_locator))
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()