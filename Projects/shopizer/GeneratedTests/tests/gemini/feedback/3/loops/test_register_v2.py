import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost/"
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        self.password = "test**11"
        self.firstname = "Test"
        self.lastname = "User"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 2. Click on the account icon/button.
        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        # 3. Select the "Register" option.
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))
        )
        register_link.click()

        # 4. Wait for the registration page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h4[text()=' Register']"))
        )

        # 5. Fill in all fields: email, password, repeat password, first name, last name.
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(self.email)

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(self.password)

        repeat_password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "repeatPassword"))
        )
        repeat_password_field.send_keys(self.password)

        firstname_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        firstname_field.send_keys(self.firstname)

        lastname_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        lastname_field.send_keys(self.lastname)

        # 6. Select a country from the dropdown.
        country_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/.."))
        )
        country_select = Select(country_dropdown)
        country_select.select_by_value("CA")

        # 7. Select a state from the dropdown.
        state_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']/.."))
        )
        state_select = Select(state_dropdown)
        state_select.select_by_value("QC")

        # 8. Submit the form.
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Register')]"))
        )
        register_button.click()

        # 9. Wait for the page to redirect and confirm registration success.
        WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        self.assertIn("/my-account", driver.current_url)

if __name__ == "__main__":
    unittest.main()