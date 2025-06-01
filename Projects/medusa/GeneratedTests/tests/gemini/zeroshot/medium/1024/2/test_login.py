import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)
        self.email = "user@test.com"
        self.password = "testuser"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click the "Account" link.
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 3. Wait for the login page to load.
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )

        # 4. Enter the email and password.
        if email_input:
            email_input.send_keys(self.email)
        else:
            self.fail("Email input not found")

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )
        if password_input:
            password_input.send_keys(self.password)
        else:
            self.fail("Password input not found")

        # 5. Click the sign-in button.
        sign_in_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
        )
        if sign_in_button:
            sign_in_button.click()
        else:
            self.fail("Sign-in button not found")

        # 6. Verify that the welcome message is present.
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message:
            welcome_text = welcome_message.text
            if welcome_text:
                self.assertEqual(welcome_text, "Hello user")
            else:
                self.fail("Welcome message text is empty")
        else:
            self.fail("Welcome message not found")

if __name__ == "__main__":
    unittest.main()