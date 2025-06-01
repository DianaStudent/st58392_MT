import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Verify that header is present
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is not present or not visible.")

        # Verify that footer is present
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is not present or not visible.")

        # Verify navigation elements
        nav_links = ["contact-link", "desktop_cart"]
        for nav_id in nav_links:
            nav_element = self.wait.until(EC.visibility_of_element_located((By.ID, nav_id)))
            self.assertIsNotNone(nav_element, f"Navigation Element {nav_id} is not present or not visible.")

        # Verify presence of login form elements
        login_form = self.wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        self.assertIsNotNone(login_form, "Login form is not present or not visible.")

        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        self.assertIsNotNone(email_input, "Email input field is not present or not visible.")

        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        self.assertIsNotNone(password_input, "Password input field is not present or not visible.")

        submit_button = self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        self.assertIsNotNone(submit_button, "Submit button is not present or not visible.")

        # Verify that "Forgot your password?" link is present
        forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        self.assertIsNotNone(forgot_password_link, "Forgot password link is not present or not visible.")

        # Verify that "Create account" link is present
        create_account_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertIsNotNone(create_account_link, "Create account link is not present or not visible.")

        # Simulate a button click
        submit_button.click()

        # Perform visual confirmation step
        # For instance, look for an error message (as expected the page will not submit successfully without valid credentials)
        try:
            error_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))
        except:
            error_message = None
        self.assertIsNotNone(error_message, "Error message should appear on failing login with empty fields.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()