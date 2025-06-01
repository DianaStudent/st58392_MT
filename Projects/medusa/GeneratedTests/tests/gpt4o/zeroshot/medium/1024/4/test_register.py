import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Wait and click on the "Account" link
        account_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='nav-account-link']"))
        )
        if not account_link.is_displayed():
            self.fail("Account link is not visible")
        account_link.click()

        # Wait and click on the "Join Us" button
        join_us_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='register-button']"))
        )
        if not join_us_button.is_displayed():
            self.fail("Join Us button is not visible")
        join_us_button.click()

        # Wait for and fill in the registration form
        first_name_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-testid='first-name-input']"))
        )
        if not first_name_input.is_displayed():
            self.fail("First name input is not visible")
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.XPATH, "//input[@data-testid='last-name-input']")
        if not last_name_input.is_displayed():
            self.fail("Last name input is not visible")
        last_name_input.send_keys("test")

        email_input = driver.find_element(By.XPATH, "//input[@data-testid='email-input']")
        if not email_input.is_displayed():
            self.fail("Email input is not visible")
        email_input.send_keys(f"user_{int(time.time())}@test.com")

        password_input = driver.find_element(By.XPATH, "//input[@data-testid='password-input']")
        if not password_input.is_displayed():
            self.fail("Password input is not visible")
        password_input.send_keys("testuser")

        # Click on the register button to submit the form
        register_button = driver.find_element(By.XPATH, "//button[@data-testid='register-button']")
        if not register_button.is_displayed():
            self.fail("Register button is not visible")
        register_button.click()

        # Verify registration success by checking for welcome message
        welcome_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='welcome-message']"))
        )
        if not welcome_message.is_displayed():
            self.fail("Welcome message is not visible")
        self.assertIn("Hello user", welcome_message.text)

if __name__ == "__main__":
    unittest.main()