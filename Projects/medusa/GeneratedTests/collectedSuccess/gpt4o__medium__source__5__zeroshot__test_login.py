import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        # Already done in setup

        # Step 2: Click the "Account" link
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_link.click()

        # Step 3: Wait for the login page to load
        login_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']")))

        # Step 4: Enter the email and password
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        self.assertTrue(email_input.is_displayed() and email_input.get_attribute('type') == 'email', "Email input is missing or incorrect")
        email_input.send_keys("user@test.com")

        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        self.assertTrue(password_input.is_displayed() and password_input.get_attribute('type') == 'password', "Password input is missing or incorrect")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        self.assertTrue(sign_in_button.is_displayed(), "Sign-in button is missing")
        sign_in_button.click()

        # Step 6: Verify that the welcome message is present
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message'][data-value='user']")))
        self.assertTrue(welcome_message.is_displayed(), "Welcome message is not displayed")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()