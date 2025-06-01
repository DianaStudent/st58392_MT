import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_button.click()
        
        # Click the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='register-button']")))
        join_us_button.click()
        
        # Fill in registration fields
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        
        # Fill the form
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        
        # Generate a unique email for testing
        import time
        unique_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(unique_email)
        
        password_input.send_keys("testuser")
        
        # Submit the form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        register_button.click()
        
        # Verify registration success by checking the welcome message
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except Exception as e:
            self.fail(f"Registration failed: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()