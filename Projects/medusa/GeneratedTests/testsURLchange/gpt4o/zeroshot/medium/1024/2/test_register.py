import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
    
    def test_user_registration(self):
        driver = self.driver
        
        # Wait and click on "Account" link
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]'))
        )
        account_link.click()
        
        # Wait and click on "Join us" button
        join_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]'))
        )
        join_button.click()
        
        # Fill in registration form
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]'))
        ).send_keys("user")
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="last-name-input"]'))
        ).send_keys("test")
        
        # Generate a dynamic email
        email = f"user_{int(time.time())}@test.com"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="email-input"]'))
        ).send_keys(email)
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="password-input"]'))
        ).send_keys("testuser")
        
        # Submit the form
        register_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]'))
        )
        register_button.click()
        
        # Verify the success of registration
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'))
        )
        
        if welcome_message is None or not welcome_message.text:
            self.fail("Registration failed, welcome message not found.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()