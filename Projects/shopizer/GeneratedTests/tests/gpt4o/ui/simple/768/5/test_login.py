import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for and check the presence of the logo
            logo = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img"))
            )

            # Wait for and check the presence of the navigation bar
            navbar = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-menu nav"))
            )

            # Wait for and check the presence of the language selector
            language_selector = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.language-currency-wrap div.language-style"))
            )

            # Wait for and check the presence of the login button
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
            )

            # Wait for and check the presence of the register button
            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
            )

            # Wait for and check the presence of account setting icon
            account_icon = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active"))
            )

            # Wait for and check the presence of the cookie consent button
            cookie_consent_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )

            # Wait for and check the presence of the login form (email and password fields)
            login_form_email = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            login_form_password = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

if __name__ == "__main__":
    unittest.main()