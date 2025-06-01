import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")        

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the homepage and click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_button.click()

        # Click on the "Join Us" button
        join_us_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="register-button"]')))
        join_us_button.click()

        # Fill in the registration form
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="first-name-input"]')))
        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name-input"]')
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
        
        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        email_input.send_keys(f"user_{int(time.time())}@test.com")  # Dynamically generated email
        password_input.send_keys("testuser")

        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="register-button"]')
        register_button.click()

        # Verify registration success by checking the presence of "Hello user"
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        
        if not welcome_message or "Hello user" not in welcome_message.text:
            self.fail("Registration failed - 'Hello user' message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()