import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
    
    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_are_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header is visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header:
            self.fail("Header is not visible")
        
        # Check footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer:
            self.fail("Footer is not visible")
        
        # Check navigation is visible
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        if not nav:
            self.fail("Navigation is not visible")
        
        # Check email input field is visible
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        if not email_input:
            self.fail("Email input field is not visible")
        
        # Check password input field is visible
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        if not password_input:
            self.fail("Password input field is not visible")
        
        # Check sign-in button is visible
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        if not sign_in_button:
            self.fail("Sign-in button is not visible")

        # Check register link is visible
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        if not register_link:
            self.fail("Register link is not visible")

        # Check forgot password link is visible
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        if not forgot_password_link:
            self.fail("Forgot password link is not visible")
        
        # Interact with show password button
        show_password_button = driver.find_element(By.CSS_SELECTOR, "button[data-action='show-password']")
        show_password_button.click()
        
        # Confirm that clicking show password button had a visual effect
        # Normally would confirm password visibility/toggle effect

if __name__ == "__main__":
    unittest.main()