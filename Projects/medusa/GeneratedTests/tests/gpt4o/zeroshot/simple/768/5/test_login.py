import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to login page
            account_link = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']"))
            )
            account_link.click()

            # Enter email
            email_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")

            # Enter password
            password_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']"))
            )
            password_input.send_keys("testuser")

            # Click sign in
            sign_in_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='sign-in-button']"))
            )
            sign_in_button.click()

            # Confirm login success by checking the welcome message
            welcome_message = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message'][data-value='user']"))
            )
            self.assertIsNotNone(welcome_message)

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()