import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Accept cookies
        try:
            cookie_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # 2. Click on the account icon/button.
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))
        )
        # Use ActionChains to click the element
        actions = ActionChains(driver)
        actions.move_to_element(register_link).click().perform()

        # 4. Wait for the registration page to load.
        self.wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        password = "test**11"
        firstname = "Test"
        lastname = "User"

        email_field = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        repeat_password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
        firstname_field = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        lastname_field = self.wait.until(EC.presence_of_element_located((By.NAME, "lastName")))

        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)

        # 6. Select a first country from the dropdown and wait for region/state dropdown to load.
        country_select = Select(self.wait.until(EC.presence_of_element_located((By.XPATH, "//select[./option[text()='Select a country']]"))))
        country_select.select_by_value("CA")

        # 7. Select a first state only after selecting country
        state_select = Select(self.wait.until(EC.presence_of_element_located((By.XPATH, "//select[./option[text()='Select a state']]"))))
        state_select.select_by_value("QC")

        # 8. Submit the form.
        register_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Register')]")))
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        self.wait.until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)


if __name__ == "__main__":
    unittest.main()