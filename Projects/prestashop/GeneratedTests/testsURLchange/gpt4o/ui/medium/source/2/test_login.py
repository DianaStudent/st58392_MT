import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
    
    def test_ui_elements(self):
        driver = self.driver

        # Check the header
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )
            self.assertTrue(header)
        except:
            self.fail("Header is not present or visible")

        # Check the login form
        try:
            login_form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "login-form"))
            )
            self.assertTrue(login_form)
        except:
            self.fail("Login form is not present or visible")

        # Check email input
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            self.assertTrue(email_input)
        except:
            self.fail("Email input is not present or visible")

        # Check password input
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )
            self.assertTrue(password_input)
        except:
            self.fail("Password input is not present or visible")

        # Check sign in button
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "submit-login"))
            )
            self.assertTrue(sign_in_button)
            # Interact with sign in button
            sign_in_button.click()
            # Check for UI feedback
        except:
            self.fail("Sign in button is not present or visible")

        # Check register link
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here"))
            )
            self.assertTrue(register_link)
        except:
            self.fail("Register link is not present or visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()