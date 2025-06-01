import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver

        # Check header presence
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        if not header.is_displayed():
            self.fail("Header is not displayed.")

        # Check menu links
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

        for link, name in zip([home_link, tables_link, chairs_link], ['Home', 'Tables', 'Chairs']):
            if not link.is_displayed():
                self.fail(f"{name} link is not displayed.")

        # Check login/register links
        account_button = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

        for link, name in zip([login_link, register_link], ['Login', 'Register']):
            if not link.is_displayed():
                self.fail(f"{name} link is not displayed.")

        # Navigate to the register page
        register_link.click()
        self.wait.until(EC.url_contains("/register"))

        # Check register form fields
        form_fields = [
            'email', 'password', 'repeatPassword', 'firstName', 'lastName', 'stateProvince'
        ]

        for field_name in form_fields:
            field = self.wait.until(
                EC.visibility_of_element_located((By.NAME, field_name))
            )
            if not field.is_displayed():
                self.fail(f"Form field {field_name} is not displayed.")

        # Accept cookies
        cookie_consent_button = self.wait.until(
            EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
        )
        if not cookie_consent_button.is_displayed():
            self.fail("Cookie consent button is not displayed.")
        cookie_consent_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()