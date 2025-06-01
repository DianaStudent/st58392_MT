import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        try:
            # Find and click the 'Account' link
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()

            # Find and click the 'Join us' button
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_button.click()

            # Generate a unique email address
            unique_id = str(uuid.uuid4())
            email = f"user_{unique_id}@test.com"

            # Find the input fields and fill them
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
            )
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='last-name-input']"))
            )
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
            )
            phone_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='phone-input']"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='password-input']"))
            )

            first_name_input.send_keys("user")
            last_name_input.send_keys("test")
            email_input.send_keys(email)
            phone_input.send_keys("123-456-7890")
            password_input.send_keys("testuser")

            # Find and click the 'Join' button
            join_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            join_button.click()

            # Wait for the welcome message to appear
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
            )

            # Assert that the welcome message is present
            self.assertEqual(welcome_message.text, "Hello user")

        except Exception as e:
            self.fail(f"An error occurred: {e}")


if __name__ == "__main__":
    unittest.main()