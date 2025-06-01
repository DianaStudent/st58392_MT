import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class MedusaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" button
        try:
            account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_button.click()
        except Exception:
            self.fail("Failed to locate or click the Account button")

        # Step 3: Wait for the login page to load
        try:
            login_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']")))
        except Exception:
            self.fail("Failed to load the login page")

        # Step 4: Enter the email and password
        try:
            email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']")))

            email_input.send_keys("user@test.com")
            password_input.send_keys("testuser")
        except Exception:
            self.fail("Failed to enter email or password")

        # Step 5: Click the sign-in button
        try:
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()
        except Exception:
            self.fail("Failed to click the sign-in button")

        # Step 6: Verify that the welcome message "Hello user" is present
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            actual_text = welcome_message.text.strip()
            self.assertEqual(actual_text, "Hello user", "Welcome message is not displayed or incorrect")
        except Exception:
            self.fail("Failed to verify the welcome message")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()