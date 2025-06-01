import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Navigate to login page
        try:
            account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()
        except:
            self.fail("Account link not found or not clickable.")

        # Enter credentials on login page
        try:
            email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")

            email_input.send_keys("user@test.com")
            password_input.send_keys("testuser")
            sign_in_button.click()
        except:
            self.fail("Failed to enter credentials or sign-in button not found.")

        # Verify successful login
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertIn("Hello user", welcome_message.text)
        except:
            self.fail("Welcome message not found after login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()