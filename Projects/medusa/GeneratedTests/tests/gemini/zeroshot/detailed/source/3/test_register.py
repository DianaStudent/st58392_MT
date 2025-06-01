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
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)
        self.email = f"user_{uuid.uuid4().hex}@test.com"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Click the "Account" button
        account_link_locator = (By.CSS_SELECTOR, '[data-testid="nav-account-link"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(account_link_locator))
        account_link = driver.find_element(*account_link_locator)
        if account_link:
            account_link.click()
        else:
            self.fail("Account link not found")

        # 2. Click the "Join us" button
        register_button_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(register_button_locator))
        register_button = driver.find_element(*register_button_locator)
        if register_button:
            register_button.click()
        else:
            self.fail("Join us button not found")

        # 3. Fill in the registration form
        first_name_input_locator = (By.CSS_SELECTOR, '[data-testid="first-name-input"]')
        last_name_input_locator = (By.CSS_SELECTOR, '[data-testid="last-name-input"]')
        email_input_locator = (By.CSS_SELECTOR, '[data-testid="email-input"]')
        password_input_locator = (By.CSS_SELECTOR, '[data-testid="password-input"]')
        register_submit_locator = (By.CSS_SELECTOR, '[data-testid="register-button"]')

        WebDriverWait(driver, 20).until(EC.presence_of_element_located(first_name_input_locator))
        first_name_input = driver.find_element(*first_name_input_locator)
        last_name_input = driver.find_element(*last_name_input_locator)
        email_input = driver.find_element(*email_input_locator)
        password_input = driver.find_element(*password_input_locator)
        register_submit = driver.find_element(*register_submit_locator)

        if first_name_input and last_name_input and email_input and password_input and register_submit:
            first_name_input.send_keys("user")
            last_name_input.send_keys("test")
            email_input.send_keys(self.email)
            password_input.send_keys("testuser")
            register_submit.click()
        else:
            self.fail("One or more registration form elements not found")

        # 4. Verify registration success
        welcome_message_locator = (By.CSS_SELECTOR, '[data-testid="welcome-message"]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(welcome_message_locator))
        welcome_message = driver.find_element(*welcome_message_locator)

        if welcome_message:
            self.assertEqual(welcome_message.text, "Hello user", "Registration failed: Welcome message not found")
        else:
            self.fail("Welcome message element not found")

if __name__ == "__main__":
    unittest.main()