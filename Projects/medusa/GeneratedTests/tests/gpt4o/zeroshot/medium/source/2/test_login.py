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
        self.driver.implicitly_wait(20)
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" link
        account_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-account-link']")))
        account_link.click()

        # Step 3: Wait for the login page to load and enter credentials
        email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='email-input']")))
        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='password-input']")))

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='sign-in-button']")))
        sign_in_button.click()

        # Step 6: Verify that the welcome message is present
        welcome_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='welcome-message']")))
        if not welcome_message or not welcome_message.text:
            self.fail("Welcome message is missing or empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()