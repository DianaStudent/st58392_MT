import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageUITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Verify 'Register' button
            register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.register-button')))
            
            # Verify 'Email' input field
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#Email')))
            
            # Verify 'Password' input field
            password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#Password')))
            
            # Verify 'Log in' button
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-button')))
            
            # Verify 'Remember me?' checkbox
            remember_me_checkbox = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#RememberMe')))

            # Verify 'Forgot password?' link
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot password?')))

            # Verify 'Search store' input field
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#small-searchterms')))
            
            # Verify 'Search' button
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-box-button')))
            
        except Exception as e:
            self.fail(f"UI element missing or not visible: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()