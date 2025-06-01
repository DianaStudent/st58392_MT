import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_login_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify presence of header logo
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo img")))
        except:
            self.fail("Header logo not found or not visible")

        # Verify presence of 'Welcome, Please Sign In!' title
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-title h1")))
        except:
            self.fail("Title 'Welcome, Please Sign In!' not found or not visible")

        # Verify presence of Email input
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        except:
            self.fail("Email input not found or not visible")

        # Verify presence of Password input
        try:
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        except:
            self.fail("Password input not found or not visible")

        # Verify presence of Remember me checkbox
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "RememberMe")))
        except:
            self.fail("Remember me checkbox not found or not visible")

        # Verify presence of Log in button and interact
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.login-button")))
            login_button.click()
        except:
            self.fail("Log in button not found or not visible")

        # Check for page updates or errors after button click
        # This is a placeholder check, assuming login input with incorrect data will prompt an error.
        try:
            error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".field-validation-error")))
        except:
            pass  # No error message visible might mean the UI adjusted for a correct input test

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()