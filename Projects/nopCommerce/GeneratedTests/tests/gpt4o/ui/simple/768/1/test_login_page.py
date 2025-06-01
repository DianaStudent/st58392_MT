import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check presence of the header
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        self.assertIsNotNone(header, "Header is not present and visible.")

        # Check presence of the login page title
        page_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.page-title > h1')))
        self.assertEqual(page_title.text, "Welcome, Please Sign In!")

        # Check presence of 'New Customer' section
        new_customer_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.new-wrapper .title')))
        self.assertEqual(new_customer_title.text, "New Customer")

        # Check 'Register' button
        register_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.register-button')))
        self.assertTrue(register_button.is_displayed(), "Register button is not visible.")

        # Check 'Returning Customer' section
        returning_customer_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.returning-wrapper .title')))
        self.assertEqual(returning_customer_title.text, "Returning Customer")

        # Check 'Email' input field
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
        self.assertTrue(email_input.is_displayed(), "Email input field is not visible.")

        # Check 'Password' input field
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
        self.assertTrue(password_input.is_displayed(), "Password input field is not visible.")

        # Check 'Remember me' checkbox
        remember_me_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, 'RememberMe')))
        self.assertTrue(remember_me_checkbox.is_displayed(), "Remember me checkbox is not visible.")

        # Check 'Forgot password?' link
        forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot password?')))
        self.assertTrue(forgot_password_link.is_displayed(), "Forgot password? link is not visible.")

        # Check 'Log in' button
        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.login-button')))
        self.assertTrue(login_button.is_displayed(), "Log in button is not visible.")

        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is not present and visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()