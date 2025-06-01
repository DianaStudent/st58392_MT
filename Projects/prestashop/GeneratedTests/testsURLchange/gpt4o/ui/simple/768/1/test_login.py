import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageUITest(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        """Test that key UI elements are present and visible."""
        driver = self.driver
        
        # Check page header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not visible on the page")
        
        # Check login form
        try:
            login_form = self.wait.until(EC.visibility_of_element_located((By.ID, 'login-form')))
        except:
            self.fail("Login form is not present")

        # Check email field
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-email')))
        except:
            self.fail("Email field is not present")

        # Check password field
        try:
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-password')))
        except:
            self.fail("Password field is not present")

        # Check login button
        try:
            login_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'submit-login')))
        except:
            self.fail("Login button is not present")

        # Check 'Forgot your password?' link
        try:
            forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot your password?')))
        except:
            self.fail("'Forgot your password?' link is not visible")

        # Check 'No account? Create one here' link
        try:
            create_account_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'No account? Create one here')))
        except:
            self.fail("'No account? Create one here' link is not visible")

    def tearDown(self):
        """Tear down the test environment."""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()