import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login_process(self):
        driver = self.driver
        
        # Navigate to the login page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))).click()
        
        # Enter email
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_input.clear()
        email_input.send_keys("admin@admin.com")
        
        # Enter password
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password_input.clear()
        password_input.send_keys("admin")
        
        # Click login
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.login-button")))
        login_button.click()
        
        # Check for logout button to confirm login success
        try:
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        except Exception as e:
            self.fail(f"Login failed or 'Log out' button not found: {str(e)}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()