import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements(self):
        driver = self.driver

        # Verify presence of header links
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ico-register"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ico-login"))
            )
        except:
            self.fail("Header links are missing")

        # Verify search input and button
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-search-box-form"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-box-text"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
        except:
            self.fail("Search input or button is missing")

        # Verify email and password fields on the login form
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Password"))
            )
        except:
            self.fail("Login form inputs are missing")

        # Verify register and login buttons
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "register-button"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "login-button"))
            )
        except:
            self.fail("Register or Login button is missing")

        # Interact with an element
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "field-validation-valid"))
            )
        except:
            self.fail("Interaction with login button failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()