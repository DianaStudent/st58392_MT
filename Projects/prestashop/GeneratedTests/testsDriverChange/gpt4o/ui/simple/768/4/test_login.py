import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check if the header is present and visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header#header")))
        except Exception as e:
            self.fail(f"Header is not present or not visible: {e}")

        # Check if the login form fields are present and visible
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except Exception as e:
            self.fail(f"Email field is not present or not visible: {e}")
        
        try:
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except Exception as e:
            self.fail(f"Password field is not present or not visible: {e}")

        # Check if the Sign in button is present and visible
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except Exception as e:
            self.fail(f"Sign in button is not present or not visible: {e}")

        # Check if the Forgot your password link is present and visible
        try:
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        except Exception as e:
            self.fail(f"Forgot your password link is not present or not visible: {e}")

        # Check if "No account? Create one here" link is present and visible
        try:
            create_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except Exception as e:
            self.fail(f"No account? Create one here link is not present or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()