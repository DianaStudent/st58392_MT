import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click login link in the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()
        
        # Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))
        
        # Enter email
        email_field = driver.find_element(By.ID, "field-email")
        email_field.clear()
        email_field.send_keys("test@user.com")
        
        # Enter password
        password_field = driver.find_element(By.ID, "field-password")
        password_field.clear()
        password_field.send_keys("test@user1")
        
        # Click login button
        submit_button = driver.find_element(By.ID, "submit-login")
        if not submit_button or submit_button.text.strip() == "":
            self.fail("Submit button not found or has no text.")
        submit_button.click()
        
        # Wait for successful login
        user_info = wait.until(EC.presence_of_element_located((By.ID, "_desktop_user_info")))
        
        # Check for "Sign out" and username
        sign_out_link = driver.find_element(By.LINK_TEXT, "Sign out")
        username_display = driver.find_element(By.XPATH, "//span[contains(text(),'test user')]")
        
        if not sign_out_link or sign_out_link.text.strip() == "":
            self.fail("Sign out button not found or has no text.")
        
        if not username_display or username_display.text.strip() == "":
            self.fail("Username not found or has no text.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()