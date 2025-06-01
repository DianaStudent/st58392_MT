import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMedusaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click the "Account" link to navigate to the login page
        try:
            account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']")))
            account_link.click()
        except Exception as e:
            self.fail("Failed to find or click on account link: " + str(e))

        # Enter email
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']")))
            email_input.send_keys("user@test.com")
        except Exception as e:
            self.fail("Failed to find or enter email: " + str(e))

        # Enter password
        try:
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            password_input.send_keys("testuser")
        except Exception as e:
            self.fail("Failed to find or enter password: " + str(e))

        # Click on Sign in button
        try:
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()
        except Exception as e:
            self.fail("Failed to find or click sign in button: " + str(e))

        # Confirm login success - check presence of the welcome message
        try:
            welcome_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']")))
            self.assertTrue(welcome_message.is_displayed(), "Welcome message not displayed.")
        except Exception as e:
            self.fail("Failed to confirm login success, welcome message not found: " + str(e))

if __name__ == "__main__":
    unittest.main()