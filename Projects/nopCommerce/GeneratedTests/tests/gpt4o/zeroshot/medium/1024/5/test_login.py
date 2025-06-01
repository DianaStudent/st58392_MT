import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        
        # Verify 'My account' link exists before clicking
        my_account_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        if not my_account_link.is_displayed():
            self.fail("My account link is not present")
        
        # Click on "My account" which should navigate to the login page
        my_account_link.click()
        
        # Wait for login page title to appear
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        
        # Verify email input field exists
        email_input = driver.find_element(By.ID, "Email")
        if not email_input.is_displayed():
            self.fail("Email input field is not present")
        
        # Enter email
        email_input.clear()
        email_input.send_keys("admin@admin.com")
        
        # Verify password input field exists
        password_input = driver.find_element(By.ID, "Password")
        if not password_input.is_displayed():
            self.fail("Password input field is not present")
        
        # Enter password
        password_input.clear()
        password_input.send_keys("admin")
        
        # Verify login button exists before clicking
        login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
        if not login_button.is_displayed():
            self.fail("Login button is not present")
        
        # Submit the form
        login_button.click()
        
        # Verify the "Log out" button is present after login
        logout_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        if not logout_link.is_displayed():
            self.fail("Log out link not found, login may have failed")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()