import unittest
import uuid
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

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the home page.
        # 2. Click on the account icon/button.
        account_button_locator = (By.CLASS_NAME, "account-setting-active")
        self.wait.until(EC.presence_of_element_located(account_button_locator)).click()

        # 3. Select the "Register" option.
        register_link_locator = (By.LINK_TEXT, "Register")
        self.wait.until(EC.presence_of_element_located(register_link_locator)).click()

        # 4. Wait for the registration page to load.
        register_form_locator = (By.NAME, "email")
        self.wait.until(EC.presence_of_element_located(register_form_locator))

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        first_name = "Test"
        last_name = "User"

        email_field_locator = (By.NAME, "email")
        password_field_locator = (By.NAME, "password")
        repeat_password_field_locator = (By.NAME, "repeatPassword")
        first_name_field_locator = (By.NAME, "firstName")
        last_name_field_locator = (By.NAME, "lastName")

        self.wait.until(EC.presence_of_element_located(email_field_locator)).send_keys(email)
        self.wait.until(EC.presence_of_element_located(password_field_locator)).send_keys(password)
        self.wait.until(EC.presence_of_element_located(repeat_password_field_locator)).send_keys(password)
        self.wait.until(EC.presence_of_element_located(first_name_field_locator)).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located(last_name_field_locator)).send_keys(last_name)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_dropdown_locator = (By.XPATH, "//select/option[text()='Select a country']/../option[2]")
        country_dropdown = self.wait.until(EC.presence_of_element_located(country_dropdown_locator))
        country_dropdown.click()

        # 7. Select a first state only after selecting country and click on some place, to avoid country selector hide state selector.
        state_dropdown_locator = (By.XPATH, "//select/option[text()='Select a state']/../option[2]")
        state_dropdown = self.wait.until(EC.presence_of_element_located(state_dropdown_locator))
        state_dropdown.click()

        # Click on some place to close dropdown
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()

        # 8. Submit the form.
        register_button_locator = (By.XPATH, "//button[contains(.,'Register')]")
        self.wait.until(EC.presence_of_element_located(register_button_locator)).click()

        # 9. Wait for the page to redirect and confirm registration success.
        # Check if the URL contains "/my-account"
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()