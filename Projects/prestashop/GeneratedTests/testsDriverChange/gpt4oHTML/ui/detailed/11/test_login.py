import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSeleniumUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check for header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is missing or not visible")

        # Check for footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is missing or not visible")

        # Check for navigation elements
        try:
            nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-nav")))
        except:
            self.fail("Navigation is missing or not visible")

        # Check for input fields and buttons in login form
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except:
            self.fail("Login form elements are missing or not visible")

        # Check for form labels
        try:
            email_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for='field-email']")))
            password_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for='field-password']")))
        except:
            self.fail("Form labels are missing or not visible")

        # Interact with Sign in button
        try:
            sign_in_button.click()
        except:
            self.fail("Unable to click on the Sign in button")

        # Check for forgot password link
        try:
            forgot_password = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        except:
            self.fail("Forgot your password link is missing or not visible")

        # Check for create account link
        try:
            create_account = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("Create account link is missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()