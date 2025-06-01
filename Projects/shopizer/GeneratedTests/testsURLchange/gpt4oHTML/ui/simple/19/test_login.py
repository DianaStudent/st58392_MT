import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/")
        
    def tearDown(self):
        self.driver.quit()
        
    def test_ui_components(self):
        driver = self.driver
        
        try:
            # Check header elements
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
            )
            self.assertTrue(header.is_displayed(), "Header area not visible")
            
            # Check home link
            home_link = driver.find_element(By.LINK_TEXT, "Home")
            self.assertTrue(home_link.is_displayed(), "Home link not visible")
            
            # Check tables link
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            self.assertTrue(tables_link.is_displayed(), "Tables link not visible")
            
            # Check chairs link
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link not visible")
            
            # Check login link
            login_link = driver.find_element(By.LINK_TEXT, "Login")
            self.assertTrue(login_link.is_displayed(), "Login link not visible")
            
            # Check register link
            register_link = driver.find_element(By.LINK_TEXT, "Register")
            self.assertTrue(register_link.is_displayed(), "Register link not visible")
        
        except Exception as e:
            self.fail(f"UI components verification failed: {str(e)}")
    
    def test_login_page_elements(self):
        driver = self.driver
        driver.get("http://localhost/login")
        
        try:
            # Check login form
            login_form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "login-form-container"))
            )
            self.assertTrue(login_form.is_displayed(), "Login form not visible")
            
            # Check email input
            email_input = driver.find_element(By.NAME, "username")
            self.assertTrue(email_input.is_displayed(), "Email input not visible")
            
            # Check password input
            password_input = driver.find_element(By.NAME, "loginPassword")
            self.assertTrue(password_input.is_displayed(), "Password input not visible")
            
            # Check login button
            login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
            self.assertTrue(login_button.is_displayed(), "Login button not visible")
        
        except Exception as e:
            self.fail(f"Login page elements verification failed: {str(e)}")
    
    def test_register_page_elements(self):
        driver = self.driver
        driver.get("http://localhost/register")
        
        try:
            # Check register form
            register_form = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "login-form-container"))
            )
            self.assertTrue(register_form.is_displayed(), "Register form not visible")
            
            # Check email input
            email_input = driver.find_element(By.NAME, "email")
            self.assertTrue(email_input.is_displayed(), "Email input not visible")
            
            # Check password input
            password_input = driver.find_element(By.NAME, "password")
            self.assertTrue(password_input.is_displayed(), "Password input not visible")
            
            # Check repeat password input
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            self.assertTrue(repeat_password_input.is_displayed(), "Repeat password input not visible")
            
            # Check register button
            register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
            self.assertTrue(register_button.is_displayed(), "Register button not visible")
        
        except Exception as e:
            self.fail(f"Register page elements verification failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()