import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click the "Account" button
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]')))
        account_link.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="login-page"]')))

        # Step 4: Enter the email and password
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="email-input"]')))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="password-input"]')))

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')))
        sign_in_button.click()

        # Step 6: Verify that the welcome message "Hello user" is present
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]')))

        self.assertTrue(welcome_message.is_displayed(), "Welcome message is not displayed")
        self.assertEqual(welcome_message.text, "Hello user", "Welcome message text does not match")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()