import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # or use any other WebDriver like Firefox
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        driver = self.driver

        try:
            # Navigate to login page
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()

            # Enter email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            email_input.send_keys("user@test.com")

            # Enter password
            password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
            password_input.send_keys("testuser")

            # Click sign in
            sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
            sign_in_button.click()

            # Confirm login success
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )
            self.assertIn("Hello user", welcome_message.text)

        except TimeoutException:
            self.fail("Timed out waiting for elements to be available.")
        except Exception as e:
            self.fail(f"An error occurred: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()