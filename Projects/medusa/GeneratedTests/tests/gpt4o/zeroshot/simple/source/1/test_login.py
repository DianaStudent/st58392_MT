import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMedusaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        try:
            # Navigate to the login page
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()

            # Wait for login page to load and input email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")

            # Input password
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            password_input.send_keys("testuser")

            # Click the sign-in button
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()

            # Confirm login was successful by checking the presence of the welcome message
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message'][data-value='user']"))
            )
            self.assertTrue(welcome_message.is_displayed())

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()