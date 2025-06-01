import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = "http://localhost:8000/dk"

    def test_user_registration(self):
        driver = self.driver

        # Open the homepage
        driver.get(self.base_url)

        # Wait and click the "Account" link
        account_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
        )
        account_link.click()

        # Wait and click the "Join Us" button
        join_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
        )
        join_button.click()

        # Fill in all fields
        first_name_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='first-name-input']"))
        )
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='last-name-input']")
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='email-input']")
        unique_email = f"user_{int(time.time())}@test.com"
        email_input.send_keys(unique_email)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        password_input.send_keys("testuser")

        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='register-button']")
        register_button.click()

        # Verify registration success by checking presence of welcome message
        welcome_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message']"))
        )

        # Check the content is not empty for assertion
        if welcome_message.text.strip() == "":
            self.fail("Registration success message is missing or empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()