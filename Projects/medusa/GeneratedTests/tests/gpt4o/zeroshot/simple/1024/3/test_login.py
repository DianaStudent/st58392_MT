import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver

        # Navigate to the login page
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except:
            self.fail("Account link not found or couldn't be clicked.")

        # Enter credentials and submit the form
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")

            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            password_input.send_keys("testuser")

            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()
        except:
            self.fail("Login form elements not found or couldn't be interacted with.")

        # Confirm success by checking that the welcome message is present
        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text)
        except:
            self.fail("Welcome message not found, login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()