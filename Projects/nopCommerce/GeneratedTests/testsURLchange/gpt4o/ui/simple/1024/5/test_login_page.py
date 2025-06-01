import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/login?returnUrl=%2F')
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        try:
            # Check for the presence and visibility of the header
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            self.assertTrue(header.is_displayed())
            
            # Check for the presence and visibility of the login form
            login_form = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-page')))
            self.assertTrue(login_form.is_displayed())
            
            # Check for the presence and visibility of the email input
            email_input = wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            self.assertTrue(email_input.is_displayed())
            
            # Check for the presence and visibility of the password input
            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.assertTrue(password_input.is_displayed())
            
            # Check for the presence and visibility of the login button
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
            self.assertTrue(login_button.is_displayed())
            
            # Check for the presence and visibility of the register button
            register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-button')))
            self.assertTrue(register_button.is_displayed())
            
            # Check for the presence and visibility of the 'Forgot password?' link
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot password?')))
            self.assertTrue(forgot_password_link.is_displayed())
            
        except Exception as e:
            self.fail(f"UI element check failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()