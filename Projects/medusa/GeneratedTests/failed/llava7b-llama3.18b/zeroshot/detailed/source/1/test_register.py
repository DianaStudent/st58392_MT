from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Open the homepage
        self.driver.get("http://localhost:8000/dk")

        # Click the "Account" button in the right left corner
        account_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='account-button']"))
        )
        account_button.click()

        # Click the "Join Us" button below the login form
        join_us_button = self.driver.find_element(By.XPATH, "//button[@data-testid='join-us-button']")
        join_us_button.click()

        # Fill in all fields: first name, last name, and password from credentials, generate unique email.
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='first-name-input']"))
        )
        first_name_input.send_keys("user")

        last_name_input = self.driver.find_element(By.XPATH, "//input[@data-testid='last-name-input']")
        last_name_input.send_keys("test")

        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='email-input']"))
        )
        email_input.send_keys("user" + str(123456789) + "@example.com") # generate unique email

        password_input = self.driver.find_element(By.XPATH, "//input[@data-testid='password-input']")
        password_input.send_keys("testuser")

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-button']"))
        )
        submit_button.click()

        # Verify registration success by checking presence of welcome message "Hello user".
        welcome_message = self.driver.find_element(By.XPATH, "//h2[@data-testid='welcome-message']")
        self.assertIsNotNone(welcome_message)
        self.assertTrue(welcome_message.text == "Hello user")

if __name__ == "__main__":
    unittest.main()