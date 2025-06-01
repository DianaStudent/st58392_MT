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
        self.driver.get('http://max/login?returnUrl=%2F')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header')))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer')))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check main navigation menu
        nav_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.top-menu.notmobile')))
        self.assertIsNotNone(nav_menu, "Main navigation menu is not visible")

        # Check login form elements
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
        self.assertIsNotNone(email_input, "Email input is not visible")

        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
        self.assertIsNotNone(password_input, "Password input is not visible")

        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.login-button')))
        self.assertIsNotNone(login_button, "Login button is not visible")

        # Check the "Remember Me" checkbox
        remember_me_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, 'RememberMe')))
        self.assertIsNotNone(remember_me_checkbox, "\"Remember Me\" checkbox is not visible")

        # Check the "Forgot password?" link
        forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot password?')))
        self.assertIsNotNone(forgot_password_link, "\"Forgot password?\" link is not visible")

        # Check Register button
        register_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.register-button')))
        self.assertIsNotNone(register_button, "Register button is not visible")

        # Interact with elements
        login_button.click()

        # Confirm that the UI reacts visually (email validation alert expected)
        alert = self.wait.until(EC.alert_is_present())
        self.assertIsNotNone(alert, "Expected alert is not present when login is clicked without credentials")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()