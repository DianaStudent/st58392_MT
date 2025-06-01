import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        # Setting up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check visibility of header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible.")

        # Check visibility of footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible.")

        # Check visibility of navigation menu
        try:
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Navigation menu is not visible.")
        
        # Check visibility of email and password fields
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except:
            self.fail("Email field is not visible.")

        try:
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Password field is not visible.")

        # Check visibility of Sign In button
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except:
            self.fail("Sign In button is not visible.")

        # Check visibility of 'Forgot your password?' link
        try:
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        except:
            self.fail("'Forgot your password?' link is not visible.")

        # Check visibility of 'No account? Create one here' link
        try:
            create_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("'No account? Create one here' link is not visible.")

        # Interact with Sign In button and confirm UI reaction
        sign_in_button.click()

        # Ensure navigation to the correct page or error message appears (Stub example)
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-content")))
        except:
            self.fail("The login action did not produce the expected UI effect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()