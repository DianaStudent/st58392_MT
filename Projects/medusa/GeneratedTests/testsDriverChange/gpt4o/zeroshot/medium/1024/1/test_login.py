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
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click the "Account" link
        account_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        if not account_link:
            self.fail("Account link not found or not clickable.")
        account_link.click()

        # Wait for the login page to load
        email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="email-input"]')))
        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="password-input"]')))
        sign_in_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')))

        if not (email_input and password_input and sign_in_button):
            self.fail("Login form elements are missing.")

        # Enter the email and password
        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Click the sign-in button
        sign_in_button.click()

        # Verify that the welcome message is present
        welcome_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        if not welcome_message:
            self.fail("Welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()