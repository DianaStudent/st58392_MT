import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MedusaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        
        try:
            # Navigate to login page via 'Account' link
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
            
            # Input email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")
            
            # Input password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )
            password_input.send_keys("testuser")
            
            # Submit login form
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()
            
            # Confirm successful login by checking for welcome message
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message'][data-value='user']"))
            )
        
        except Exception as e:
            self.fail(f"Test failed due to missing element or timeout: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()