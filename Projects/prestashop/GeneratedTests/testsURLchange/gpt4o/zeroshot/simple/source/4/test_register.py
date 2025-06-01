import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class UserRegistrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_user_registration(self):
        driver = self.driver
        
        # Navigate to login page
        sign_in_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()
        
        # Navigate to registration page
        create_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        create_account_link.click()
        
        # Fill registration form
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        last_name_field = driver.find_element(By.ID, "field-lastname")
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        
        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        email_field.send_keys(f"test_user_{int(time.time())}@example.com")
        password_field.send_keys("test@user1")
        
        # Check required checkboxes
        terms_checkbox.click()
        privacy_checkbox.click()
        
        # Submit the form
        save_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.form-control-submit")
        save_button.click()
        
        # Check if registration was successful by verifying the presence of "Sign out"
        try:
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        except:
            self.fail("Registration failed: 'Sign out' link not found")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()