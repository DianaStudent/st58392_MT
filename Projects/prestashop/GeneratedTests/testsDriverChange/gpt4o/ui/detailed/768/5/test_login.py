import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check if header is present and visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is missing")

        # Check main navigation menu
        top_menu = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_top_menu")))
        self.assertIsNotNone(top_menu, "Top menu is missing")

        # Check if footer is present and visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Verify the presence of login form and its fields
        login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        self.assertIsNotNone(login_form, "Login form is missing")
        
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        self.assertIsNotNone(email_field, "Email field is missing")

        password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        self.assertIsNotNone(password_field, "Password field is missing")

        # Verify the presence of buttons
        submit_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        self.assertIsNotNone(submit_button, "Submit button is missing")

        # Verify presence of 'Forgot your password?' link
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        self.assertIsNotNone(forgot_password_link, "'Forgot your password?' link is missing")

        # Verify presence of registration link
        registration_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertIsNotNone(registration_link, "Registration link is missing")

        # Interact with UI elements and check the reactions
        submit_button.click()
        # Here you can add more interaction as needed like checking for error messages

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()