import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        # Verify Header is present and visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except:
            self.fail("Header not found or not visible")

        # Verify Email field is present and visible
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-email')))
        except:
            self.fail("Email field not found or not visible")

        # Verify Password field is present and visible
        try:
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-password')))
        except:
            self.fail("Password field not found or not visible")
        
        # Verify Sign in button is present and visible
        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'submit-login')))
        except:
            self.fail("Sign in button not found or not visible")

        # Verify forgot password link is present and visible
        try:
            forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot your password?')))
        except:
            self.fail("Forgot password link not found or not visible")

        # Verify Registration link is present and visible
        try:
            registration_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'No account? Create one here')))
        except:
            self.fail("Registration link not found or not visible")

        # Verify Cart icon is present and visible
        try:
            cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping-cart')))
        except:
            self.fail("Cart icon not found or not visible")

        # Verify Search bar is present and visible
        try:
            search_bar = self.wait.until(EC.visibility_of_element_located((By.NAME, 's')))
        except:
            self.fail("Search bar not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()