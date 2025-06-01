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
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 2. Click the "Account" button
        account_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_link.click()

        # 3. Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='login-page']")))

        # 4. Enter the email
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        email_input.send_keys("user@test.com")

        # Enter the password
        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        password_input.send_keys("testuser")

        # 5. Click the sign-in button
        sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        sign_in_button.click()

        # 6. Verify that the welcome message "Hello user" is present
        try:
            welcome_message = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text)
        except:
            self.fail("The welcome message 'Hello user' was not found.")

if __name__ == "__main__":
    unittest.main()