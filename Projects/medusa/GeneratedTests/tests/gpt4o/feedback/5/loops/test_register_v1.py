import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the homepage
        homepage_loaded = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body")))
        if not homepage_loaded:
            self.fail("Homepage did not load properly")
        
        # Step 2: Click the "Account" button
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_button.click()
        
        # Step 3: Click the "Join Us" button
        join_us_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-button']")))
        join_us_button.click()
        
        # Step 4: Fill in registration form
        first_name_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='last-name-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(f"user_{int(time.time())}@test.com")
        password_input.send_keys("testuser")
        
        # Step 5: Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='register-button']")
        register_button.click()
        
        # Step 6: Verify registration success
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        
        if not welcome_message or welcome_message.text.strip() != "Hello user":
            self.fail("Registration was not successful or welcome message is missing or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()