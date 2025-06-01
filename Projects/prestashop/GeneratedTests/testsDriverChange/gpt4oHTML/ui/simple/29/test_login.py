import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check main UI components on the login page
        try:
            # Header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header, "Header is not present or not visible.")

            # Login Form
            login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
            self.assertIsNotNone(login_form, "Login form is not present or not visible.")

            # Email Field
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertIsNotNone(email_field, "Email field is not present or not visible.")

            # Password Field
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertIsNotNone(password_field, "Password field is not present or not visible.")
            
            # Sign In Button
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertIsNotNone(sign_in_button, "Sign in button is not present or not visible.")

            # Forgot Password Link
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            self.assertIsNotNone(forgot_password_link, "Forgot password link is not present or not visible.")

            # No Account Link
            no_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            self.assertIsNotNone(no_account_link, "No account? Create one here link is not present or not visible.")

            # Top Menu links
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.assertIsNotNone(clothes_link, "Clothes link is not present or not visible.")

            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.assertIsNotNone(accessories_link, "Accessories link is not present or not visible.")

            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            self.assertIsNotNone(art_link, "Art link is not present or not visible.")
        
        except Exception as e:
            self.fail(f"UI component check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()