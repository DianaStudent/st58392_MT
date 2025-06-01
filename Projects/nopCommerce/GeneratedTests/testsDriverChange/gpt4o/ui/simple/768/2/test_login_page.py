import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_page_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            header_links = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-links')))
            self.assertTrue(header_links.is_displayed())
        except:
            self.fail("Header links not visible")

        # Check register button
        try:
            register_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.register-block .register-button')))
            self.assertTrue(register_button.is_displayed())
        except:
            self.fail("Register button not visible")

        # Check login form elements
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            self.assertTrue(email_input.is_displayed())
        except:
            self.fail("Email input not visible")

        try:
            password_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.assertTrue(password_input.is_displayed())
        except:
            self.fail("Password input not visible")

        try:
            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-button')))
            self.assertTrue(login_button.is_displayed())
        except:
            self.fail("Login button not visible")

        # Check footer elements
        try:
            footer_info = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-info')))
            self.assertTrue(footer_info.is_displayed())
        except:
            self.fail("Footer info not visible")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()