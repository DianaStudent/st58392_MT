import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MedusaLoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        
        # Navigate to login page
        try:
            account_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to login page: {e}")

        # Enter email
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            email_input.send_keys("user@test.com")
        except Exception as e:
            self.fail(f"Failed to find or interact with email input: {e}")

        # Enter password
        try:
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to find or interact with password input: {e}")

        # Click sign-in button
        try:
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click sign-in button: {e}")

        # Confirm login success
        try:
            welcome_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
        except Exception as e:
            self.fail(f"Login was unsuccessful or welcome message not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()