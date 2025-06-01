import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page and click the "Account" link
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Step 2: Wait for the login page to load and verify the presence of the email input
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
        if not email_input:
            self.fail("Email input box not found or is empty.")

        # Step 3: Enter the email and password
        email_input.send_keys("user@test.com")

        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        if not password_input:
            self.fail("Password input box not found or is empty.")

        password_input.send_keys("testuser")

        # Step 4: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        if not sign_in_button:
            self.fail("Sign-in button not found or is empty.")

        sign_in_button.click()

        # Step 5: Verify that the welcome message is present
        welcome_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "span[data-testid='welcome-message']")
        ))
        if not welcome_message:
            self.fail("Welcome message not found or is empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()