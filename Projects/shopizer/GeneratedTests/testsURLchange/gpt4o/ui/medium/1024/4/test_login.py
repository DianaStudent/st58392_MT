import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/login')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify presence and visibility of navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//ul/li/a[@href='/']")))
        except TimeoutException:
            self.fail("Home link is not visible.")

        try:
            tables_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//ul/li/a[@href='/category/tables']")))
        except TimeoutException:
            self.fail("Tables link is not visible.")

        try:
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//ul/li/a[@href='/category/chairs']")))
        except TimeoutException:
            self.fail("Chairs link is not visible.")

        # Verify presence and visibility of login form fields
        try:
            username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        except TimeoutException:
            self.fail("Username input is not visible.")

        try:
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
        except TimeoutException:
            self.fail("Password input is not visible.")

        # Verify presence and visibility of login button
        try:
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
        except TimeoutException:
            self.fail("Login button is not visible.")

        # Verify presence of accept cookies button and interact with it
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except TimeoutException:
            self.fail("Accept cookies button is not visible or clickable.")
        
        # Verify interaction of 'Forgot Password?' link
        try:
            forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot Password?")))
            forgot_password_link.click()
            # Check if navigation to forgot password page happens
            self.assertIn("/forgot-password", driver.current_url, "Navigation to forgot-password page failed.")
        except TimeoutException:
            self.fail("'Forgot Password?' link is not visible or clickable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()