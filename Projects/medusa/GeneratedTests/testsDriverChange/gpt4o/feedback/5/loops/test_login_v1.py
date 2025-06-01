import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class MedusaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" button
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
        account_button.click()

        # Step 3: Wait for the login page to load
        login_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']")))

        # Step 4: Enter the email and password
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")

        # Step 5: Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        sign_in_button.click()

        # Step 6: Verify that the welcome message "Hello user" is present
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            actual_text = welcome_message.text.strip()
            self.assertEqual(actual_text, "Hello user", "Welcome message is not displayed or incorrect")
        except Exception as e:
            self.fail(f"Welcome message verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()