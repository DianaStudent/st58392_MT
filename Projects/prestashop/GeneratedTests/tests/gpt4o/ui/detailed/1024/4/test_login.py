import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is missing or not visible")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is missing or not visible")

        # Check form fields: Email and Password
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        self.assertIsNotNone(email_field, "Email field is missing or not visible")

        password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        self.assertIsNotNone(password_field, "Password field is missing or not visible")

        # Check buttons: Sign in
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        self.assertIsNotNone(sign_in_button, "Sign in button is missing or not visible")

        # Check links: Forgot password and Register
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        self.assertIsNotNone(forgot_password_link, "Forgot your password link is missing or not visible")

        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertIsNotNone(register_link, "Register link is missing or not visible")

        # Interact with UI element: Click Show password button
        show_password_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-action='show-password']")))
        show_password_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()