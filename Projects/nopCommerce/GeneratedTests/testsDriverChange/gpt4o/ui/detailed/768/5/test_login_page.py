import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        # Wait for header to be visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header"))
        )
        self.assertIsNotNone(header, "Header is missing.")

        # Wait for footer to be visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
        )
        self.assertIsNotNone(footer, "Footer is missing.")

        # Check for "Welcome, Please Sign In!" title
        page_title = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "page-title"))
        )
        self.assertIn("Welcome, Please Sign In!", page_title.text, "Page title is missing.")

        # Check for Email input field
        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "Email"))
        )
        self.assertIsNotNone(email_input, "Email input field is missing.")

        # Check for Password input field
        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "Password"))
        )
        self.assertIsNotNone(password_input, "Password input field is missing.")

        # Check for Remember Me checkbox
        remember_me_checkbox = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "RememberMe"))
        )
        self.assertIsNotNone(remember_me_checkbox, "Remember Me checkbox is missing.")

        # Check for Login button
        login_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "login-button"))
        )
        self.assertIsNotNone(login_button, "Login button is missing.")

        # Check for Register button
        register_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "register-button"))
        )
        self.assertIsNotNone(register_button, "Register button is missing.")

        # Interact with UI elements
        login_button.click()

        # Check for error message (Expecting a notification here due to empty form submission)
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "dialog-notifications-error"))
            )
        except:
            self.fail("Expected error message is missing.")

if __name__ == "__main__":
    unittest.main()