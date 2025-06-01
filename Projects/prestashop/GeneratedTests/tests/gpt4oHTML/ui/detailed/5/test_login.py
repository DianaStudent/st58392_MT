import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome webdriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # 1. Check if header is visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is not visible on the page")

        # 2. Check if footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible on the page")

        # 3. Check if navigation elements are visible
        nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-nav")))
        self.assertIsNotNone(nav, "Navigation is not visible on the page")

        # 4. Check presence and visibility of the login form
        login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        self.assertIsNotNone(login_form, "Login form is not visible on the page")

        # 5. Check input fields
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        self.assertIsNotNone(email_input, "Email input field is not visible on the page")

        password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        self.assertIsNotNone(password_input, "Password input field is not visible on the page")

        # 6. Check buttons
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        self.assertIsNotNone(sign_in_button, "Sign in button is not visible on the page")

        # 7. Check 'Forgot your password' link
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        self.assertIsNotNone(forgot_password_link, "Forgot your password link is not visible on the page")

        # 8. Check 'No account? Create one here' link
        no_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertIsNotNone(no_account_link, "No account? Create one here link is not visible on the page")

        # 9. Click the Sign-in Button to confirm UI reacts
        sign_in_button.click()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()