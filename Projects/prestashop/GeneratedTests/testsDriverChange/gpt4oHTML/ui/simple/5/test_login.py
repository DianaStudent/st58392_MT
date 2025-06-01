from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check login form presence
        try:
            login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        except:
            self.fail("Login form not found or not visible")

        # Check email input presence
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except:
            self.fail("Email input not found or not visible")

        # Check password input presence
        try:
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Password input not found or not visible")

        # Check Sign in button presence
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except:
            self.fail("Sign in button not found or not visible")

        # Check forgot password link presence
        try:
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        except:
            self.fail("Forgot password link not found or not visible")

        # Check registration link presence
        try:
            registration_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("Registration link not found or not visible")
        
    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()