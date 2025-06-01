import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver

        # Verify the header is present
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header not found or not visible.")

        # Verify navigation links
        try:
            nav_links = driver.find_element(By.CLASS_NAME, "top-menu")
        except:
            self.fail("Navigation links not found or not visible.")
        
        # Verify email input field
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except:
            self.fail("Email input not found or not visible.")
        
        # Verify password input field
        try:
            password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Password input not found or not visible.")

        # Verify the sign-in button
        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            sign_in_button.click()
        except:
            self.fail("Sign-in button not found or not visible.")
        
        # Verify the 'No account? Create one here' link
        try:
            create_account_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("Create account link not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()