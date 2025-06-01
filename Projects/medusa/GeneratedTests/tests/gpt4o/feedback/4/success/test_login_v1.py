import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_button.click()

        # Wait for the login page
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page']")))

        # Enter Email
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']")))
        email_input.send_keys("user@test.com")

        # Enter Password
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        password_input.send_keys("testuser")

        # Click Sign in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='sign-in-button']")
        sign_in_button.click()

        # Verify welcome message
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        
        if not welcome_message.text or "Hello user" not in welcome_message.text:
            self.fail("Welcome message not found or incorrect after login.")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()