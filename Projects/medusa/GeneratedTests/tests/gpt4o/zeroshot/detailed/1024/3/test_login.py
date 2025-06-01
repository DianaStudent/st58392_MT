import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Step 2: Click the "Account" button
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
        )
        self.assertTrue(account_button, "Account button is missing")
        account_button.click()

        # Step 3: Wait for the login page to load
        login_page = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-page']"))
        )
        self.assertTrue(login_page, "Login page did not load")

        # Step 4: Enter the email and password
        email_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']"))
        )
        self.assertTrue(email_input, "Email input is missing")
        email_input.send_keys("user@test.com")

        password_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']"))
        )
        self.assertTrue(password_input, "Password input is missing")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='sign-in-button']"))
        )
        self.assertTrue(sign_in_button, "Sign-in button is missing")
        sign_in_button.click()

        # Step 6: Verify the welcome message
        welcome_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
        )
        self.assertTrue(welcome_message, "Welcome message is missing")
        self.assertEqual(welcome_message.text, "Hello user", "Incorrect welcome message")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()