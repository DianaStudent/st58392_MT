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

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Account" link
        try:
            account_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-account-link']")))
            account_link.click()
        except Exception as e:
            self.fail(f"Failed to locate or click Account link: {str(e)}")

        # Step 3: Wait for the login page to load
        try:
            login_page = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='login-page']")))
        except Exception as e:
            self.fail(f"Login page did not load: {str(e)}")

        # Step 4: Enter the email and password
        try:
            email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='email-input']")))
            password_input = driver.find_element(By.XPATH, "//input[@data-testid='password-input']")
            email_input.send_keys("user@test.com")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail(f"Failed to enter credentials: {str(e)}")

        # Step 5: Click the sign-in button
        try:
            sign_in_button = driver.find_element(By.XPATH, "//button[@data-testid='sign-in-button']")
            sign_in_button.click()
        except Exception as e:
            self.fail(f"Failed to click the Sign-in button: {str(e)}")

        # Step 6: Verify that the welcome message is present
        try:
            welcome_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='welcome-message']")))
            if not welcome_message.text.strip():
                self.fail("Welcome message is empty.")
        except Exception as e:
            self.fail(f"Failed to find or validate the welcome message: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()