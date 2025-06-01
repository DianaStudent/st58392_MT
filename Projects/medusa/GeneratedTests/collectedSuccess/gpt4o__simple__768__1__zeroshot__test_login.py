import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your WebDriver path if necessary
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to login page
        account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_link.click()

        # Check if on login page
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="login-page"]')))
        except:
            self.fail("Login page did not load.")

        # Enter email
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="email-input"]')))
        email_input.send_keys("user@test.com")

        # Enter password
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
        password_input.send_keys("testuser")

        # Click sign in
        sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')
        sign_in_button.click()

        # Verify login success
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))
        except:
            self.fail("Login failed or welcome message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()