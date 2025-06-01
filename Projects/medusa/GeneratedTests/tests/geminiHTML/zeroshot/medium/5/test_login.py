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
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click the "Account" link.
        account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # 3. Wait for the login page to load.
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))

        # 4. Enter the email and password.
        email_input.send_keys("user@test.com")
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        password_input.send_keys("testuser")

        # 5. Click the sign-in button.
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        sign_in_button.click()

        # 6. Verify that the welcome message is present.
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            if welcome_message and welcome_message.text:
                self.assertEqual(welcome_message.text, "Hello user")
            else:
                self.fail("Welcome message element is missing or empty.")
        except Exception as e:
            self.fail(f"Welcome message not found or assertion failed: {e}")

if __name__ == "__main__":
    unittest.main()