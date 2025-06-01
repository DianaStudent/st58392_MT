from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        # Already done in setUp()

        # Step 2: Click the "Account" link
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        self.assertTrue(account_link, "Account link is missing.")
        account_link.click()

        # Step 3: Wait for the login page to load
        login_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page']")))
        self.assertTrue(login_page, "Login page didn't load.")

        # Step 4: Enter the email and password
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-input']")
        self.assertTrue(email_input, "Email input is missing.")
        email_input.send_keys("user@test.com")

        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        self.assertTrue(password_input, "Password input is missing.")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='sign-in-button']")
        self.assertTrue(sign_in_button, "Sign in button is missing.")
        sign_in_button.click()

        # Step 6: Verify that the welcome message is present
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        self.assertTrue(welcome_message, "Welcome message is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()