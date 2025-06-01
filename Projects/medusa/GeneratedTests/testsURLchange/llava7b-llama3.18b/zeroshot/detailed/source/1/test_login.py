import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Click the "Account" button in the right left corner
        account_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='account-button']"))
        )
        account_button.click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='username-input']"))
        )

        # Enter the email and password using credentials
        username_input = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='username-input']")
        username_input.send_keys("user@test.com")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='password-input']")
        password_input.send_keys("testuser")

        # Click the sign-in button
        signin_button = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='signin-button']")
        signin_button.click()

        # Verify that the welcome message "Hello user" is present
        welcome_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']"))
        )
        self.assertIsNotNone(welcome_message.text)
        self.assertEqual("Hello user", welcome_message.text)

if __name__ == "__main__":
    unittest.main()