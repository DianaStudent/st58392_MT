import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_page_ui_elements(self):
        driver = self.driver

        # Verify header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            self.assertIsNotNone(header)
        except:
            self.fail("Header is missing or not visible.")

        # Verify logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))
            self.assertIsNotNone(logo)
        except:
            self.fail("Logo is missing or not visible.")

        # Verify page title
        try:
            page_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-title")))
            self.assertIsNotNone(page_title)
        except:
            self.fail("Page title is missing or not visible.")

        # Verify login form elements
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            self.assertIsNotNone(email_input)

            password_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.assertIsNotNone(password_input)

            login_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
            self.assertIsNotNone(login_button)
        except:
            self.fail("Login form elements are missing or not visible.")

        # Verify "Register" button
        try:
            register_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-button')))
            self.assertIsNotNone(register_button)
        except:
            self.fail("Register button is missing or not visible.")

        # Verify footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            self.assertIsNotNone(footer)
        except:
            self.fail("Footer is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()