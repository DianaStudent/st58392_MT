from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class MedusaStoreLoginTest(unittest.TestCase):

    def setUp(self):
        # Setting up Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver

        try:
            # Step 2: Click the "Account" link
            account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-account-link"]'))
            )
            account_link.click()

            # Step 3: Wait for the login page to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="login-page"]'))
            )

            # Step 4: Enter the email
            email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="email-input"]')
            email_input.clear()
            email_input.send_keys("user@test.com")

            # Enter the password
            password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
            password_input.clear()
            password_input.send_keys("testuser")

            # Step 5: Click the sign-in button
            sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sign-in-button"]')
            sign_in_button.click()

            # Step 6: Verify that the welcome message is present
            welcome_message = WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span[data-testid="welcome-message"]'), "Hello user")
            )

            if not welcome_message:
                self.fail("Welcome message is not displayed or text does not match.")
        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        # Clean up and close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()