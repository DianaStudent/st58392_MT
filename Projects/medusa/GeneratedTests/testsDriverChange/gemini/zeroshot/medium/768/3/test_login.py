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

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        email = "user@test.com"
        password = "testuser"

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "Account" link.
        account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_link.click()

        # 3. Wait for the login page to load.
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
        )

        # 4. Enter the email and password.
        email_input.send_keys(email)
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
        )
        password_input.send_keys(password)

        # 5. Click the sign-in button.
        sign_in_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='sign-in-button']"))
        )
        sign_in_button.click()

        # 6. Verify that the welcome message is present.
        welcome_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        if welcome_message:
            welcome_text = welcome_message.get_attribute("data-value")
            if welcome_text and welcome_text == "user":
                pass  # Success
            else:
                self.fail("Welcome message text is incorrect.")
        else:
            self.fail("Welcome message is not present.")

if __name__ == "__main__":
    unittest.main()