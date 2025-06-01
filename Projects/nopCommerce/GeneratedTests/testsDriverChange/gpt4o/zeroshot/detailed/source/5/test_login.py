from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login_process(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to login page
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))
        if login_link:
            login_link.click()
        else:
            self.fail("Login link not found")

        # Ensure login page is loaded
        email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        
        if not email_field or not password_field:
            self.fail("Login page fields are not present")

        # Fill in Email
        email_field.send_keys("admin@admin.com")

        # Fill in Password
        password_field.send_keys("admin")
        
        # Click the Log in button
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.login-button")))
        if login_button:
            login_button.click()
        else:
            self.fail("Login button not clickable")
        
        # Check for Log out button after logging in
        logout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        if not logout_link:
            self.fail("Log out link not found. Login was unsuccessful.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()