from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestNOPCommerceUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        self.assertIsNotNone(header, "Header is missing or not visible.")

        # Check visibility of footer
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is missing or not visible.")

        # Check visibility of login form fields
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        self.assertIsNotNone(email_field, "Email input field is missing or not visible.")
        self.assertIsNotNone(password_field, "Password input field is missing or not visible.")

        # Check visibility of login button
        login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
        self.assertIsNotNone(login_button, "Login button is missing or not visible.")

        # Check visibility of register button
        register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
        self.assertIsNotNone(register_button, "Register button is missing or not visible.")

        # Check visibility of the "Remember me" checkbox
        remember_me_checkbox = wait.until(EC.visibility_of_element_located((By.ID, "RememberMe")))
        self.assertIsNotNone(remember_me_checkbox, "Remember Me checkbox is missing or not visible.")

        # Interact with login button and verify the UI reacts properly
        login_button.click()
        error_notification = wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-error")))
        self.assertTrue(error_notification.is_displayed(), "Error notification is not visible after login attempt.")

if __name__ == "__main__":
    unittest.main()