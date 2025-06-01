from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Header
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        if not header:
            self.fail("Header is not visible.")

        # Footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        if not footer:
            self.fail("Footer is not visible.")

        # Page Title
        page_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'page-title')))
        if not page_title:
            self.fail("Page title is not visible.")

        # Email input
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
        if not email_input:
            self.fail("Email input is not visible.")

        self.assertTrue(email_input.is_displayed(), "Email input is not displayed.")

        # Password input
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
        if not password_input:
            self.fail("Password input is not visible.")

        self.assertTrue(password_input.is_displayed(), "Password input is not displayed.")

        # Login button
        login_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
        if not login_button:
            self.fail("Login button is not visible.")

        self.assertTrue(login_button.is_displayed(), "Login button is not displayed.")

        # Register button
        register_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-button')))
        if not register_button:
            self.fail("Register button is not visible.")

        self.assertTrue(register_button.is_displayed(), "Register button is not displayed.")

        # Checking interactions
        register_button.click()
        self.wait.until(EC.url_contains("register"))
        
        driver.back()
        
        login_button.click()
        self.wait.until(EC.url_contains("login"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)