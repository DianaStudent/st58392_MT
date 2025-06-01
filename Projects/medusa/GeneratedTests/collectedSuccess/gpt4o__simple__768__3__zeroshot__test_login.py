from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestMedusaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Adjust the webdriver as needed
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to the Account page
            account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()

            # Enter email and password
            email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            email_input.send_keys("user@test.com")

            password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))
            password_input.send_keys("testuser")

            # Click Sign in
            sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sign-in-button']")))
            sign_in_button.click()

            # Confirm success by checking the presence of the welcome message
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertIsNotNone(welcome_message)
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()