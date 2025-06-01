import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 2: Click the "Account" link
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_link.click()
        
        # Step 3: Click the "Join Us" button
        join_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]')))
        join_button.click()
        
        # Step 4: Fill in all fields
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]')))
        first_name_input.send_keys("user")
        
        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        last_name_input.send_keys("test")
        
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        unique_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(unique_email)
        
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
        password_input.send_keys("testuser")
        
        # Step 5: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        register_button.click()
        
        # Step 6: Verify registration success by checking the presence of a welcome message
        welcome_message_locator = By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'
        welcome_message = wait.until(EC.presence_of_element_located(welcome_message_locator))
        self.assertTrue(welcome_message.is_displayed(), "Welcome message not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()