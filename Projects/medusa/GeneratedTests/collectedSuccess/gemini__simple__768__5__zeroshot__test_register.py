import unittest
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

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        try:
            account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-account-link']"))
            )
            account_link.click()
        except:
            self.fail("Account link not found")

        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='register-button']"))
            )
            register_button.click()
        except:
            self.fail("Register button not found")

        first_name_input_selector = "input[data-testid='first-name-input']"
        last_name_input_selector = "input[data-testid='last-name-input']"
        email_input_selector = "input[data-testid='email-input']"
        phone_input_selector = "input[data-testid='phone-input']"
        password_input_selector = "input[data-testid='password-input']"
        register_button_selector = "button[data-testid='register-button']"

        first_name = "user"
        last_name = "test"
        email = f"user_{uuid.uuid4().hex[:6]}@test.com"
        password = "testuser"

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, first_name_input_selector))
            )
            first_name_input.send_keys(first_name)
        except:
            self.fail("First name input not found")

        try:
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, last_name_input_selector))
            )
            last_name_input.send_keys(last_name)
        except:
            self.fail("Last name input not found")

        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, email_input_selector))
            )
            email_input.send_keys(email)
        except:
            self.fail("Email input not found")

        try:
            phone_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, phone_input_selector))
            )
            phone_input.send_keys("12345678")
        except:
            self.fail("Phone input not found")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, password_input_selector))
            )
            password_input.send_keys(password)
        except:
            self.fail("Password input not found")

        try:
            register_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, register_button_selector))
            )
            register_button.click()
        except:
            self.fail("Register button not found")

        try:
            welcome_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='welcome-message'][data-value='user']"))
            )
            self.assertEqual("Hello user", welcome_message.text)
        except:
            self.fail("Welcome message not found after registration")


if __name__ == "__main__":
    unittest.main()