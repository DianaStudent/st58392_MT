import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click the "Account" button
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if not account_button.is_displayed():
            self.fail("Account button is missing.")
        account_button.click()

        # Wait for the login page to load
        email_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )
        if not email_input.is_displayed():
            self.fail("Email input field is missing.")

        # Enter email
        email_input.send_keys("user@test.com")

        # Enter password
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        if not password_input.is_displayed():
            self.fail("Password input field is missing.")
        password_input.send_keys("testuser")

        # Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        if not sign_in_button.is_displayed():
            self.fail("Sign-in button is missing.")
        sign_in_button.click()

        # Verify the welcome message "Hello user" is present
        welcome_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )
        if not welcome_message.is_displayed():
            self.fail("Welcome message is missing.")
        self.assertIn("Hello user", welcome_message.text, "Welcome message text is incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()