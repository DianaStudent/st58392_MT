from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Set up WebDriver using the chrome driver manager.
        self.driver = webdriver.Chrome()

    def test_login(self):
        # Navigate to the home page.
        self.driver.get('http://localhost:8000/dk')

        # Click on the "Account" button in the right left corner.
        account_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="account-button"]'))
        )
        account_button.click()

        # Wait for the login page to load.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="login-form"]')))

        # Locate email and password input fields using their data-testid attributes.
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="email-input"]'))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="password-input"]'))
        )

        # Enter email and password.
        email_input.send_keys('user@test.com')
        password_input.send_keys('testuser')

        # Click the sign-in button.
        sign_in_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="sign-in-button"]'))
        )
        sign_in_button.click()

        # Wait for the welcome message to appear.
        welcome_message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]'))
        )

        # Assert that the welcome message contains "Hello user".
        self.assertIn('Hello user', welcome_message.text)

    def tearDown(self):
        # Close the browser window.
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()