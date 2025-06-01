import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver
        
        # Check header
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header.is_displayed():
            self.fail("Header is not visible.")
        
        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer.is_displayed():
            self.fail("Footer is not visible.")
        
        # Check login form
        login_form = self.wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        if not login_form.is_displayed():
            self.fail("Login form is not visible.")

        # Check email input
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        if not email_input.is_displayed():
            self.fail("Email input field is not visible.")
        
        # Check password input
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        if not password_input.is_displayed():
            self.fail("Password input field is not visible.")
        
        # Check Sign in button
        sign_in_button = self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        if not sign_in_button.is_displayed():
            self.fail("Sign in button is not visible.")

        # Check Forgot your password link
        forgot_password_link = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?"))
        )
        if not forgot_password_link.is_displayed():
            self.fail("Forgot your password link is not visible.")

        # Check Register link
        register_link = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here"))
        )
        if not register_link.is_displayed():
            self.fail("Register link is not visible.")

        # Interact with UI and check
        sign_in_button.click()
        # Confirm basic UI interaction, might need more checks in real tests
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not clickable or did not respond.")

if __name__ == "__main__":
    unittest.main()