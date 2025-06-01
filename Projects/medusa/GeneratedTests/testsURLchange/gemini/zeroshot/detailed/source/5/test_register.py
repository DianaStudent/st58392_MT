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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8000/dk"
        self.first_name = "user"
        self.last_name = "test"
        self.password = "testuser"
        self.email = f"user_{uuid.uuid4().hex}@test.com"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Click the "Account" button
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(account_link_locator))
        account_link = driver.find_element(*account_link_locator)
        account_link.click()

        # 2. Click the "Join us" button
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(register_button_locator))
        register_button = driver.find_element(*register_button_locator)
        register_button.click()

        # 3. Fill in the registration form
        first_name_input_locator = (By.CSS_SELECTOR, '[data-testid="first-name-input"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(first_name_input_locator))
        first_name_input = driver.find_element(*first_name_input_locator)
        first_name_input.send_keys(self.first_name)

        last_name_input_locator = (By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        last_name_input = driver.find_element(*last_name_input_locator)
        last_name_input.send_keys(self.last_name)

        email_input_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        email_input = driver.find_element(*email_input_locator)
        email_input.send_keys(self.email)

        password_input_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        password_input = driver.find_element(*password_input_locator)
        password_input.send_keys(self.password)

        # 4. Submit the form
        submit_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        submit_button = driver.find_element(*submit_button_locator)
        submit_button.click()

        # 5. Verify registration success
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(welcome_message_locator))
        welcome_message_element = driver.find_element(*welcome_message_locator)
        welcome_message_text = welcome_message_element.get_attribute("data-value")

        if welcome_message_text is None or welcome_message_text == "":
            self.fail("Welcome message is missing or empty.")

        self.assertEqual(welcome_message_text, "user", "Registration failed. Welcome message is incorrect.")


if __name__ == "__main__":
    unittest.main()