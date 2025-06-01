import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # 2. Click the "Account" link.
        account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Account")))
        self.assertIsNotNone(account_link, "Account link not found.")
        account_link.click()

        # 3. Click the "Join Us" button.
        join_us_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='register-button']")))
        self.assertIsNotNone(join_us_button, "Join Us button not found.")
        join_us_button.click()

        # 4. Fill in all fields: first name, last name, email, password.
        first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='first-name-input']")))
        last_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='last-name-input']")))
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='email-input']")))
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='password-input']")))

        self.assertIsNotNone(first_name_input, "First Name input not found.")
        self.assertIsNotNone(last_name_input, "Last Name input not found.")
        self.assertIsNotNone(email_input, "Email input not found.")
        self.assertIsNotNone(password_input, "Password input not found.")

        first_name = "user"
        last_name = "test"
        email = f"user_{int(time.time())}@example.com"
        password = "testuser"

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        password_input.send_keys(password)

        # 5. Submit the registration form.
        register_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='register-button']")))
        self.assertIsNotNone(register_button, "Register button not found.")
        register_button.click()

        # 6. Verify registration success by checking presence of welcome message.
        welcome_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='welcome-message']")))
        self.assertTrue(welcome_message.is_displayed(), "Welcome message not found or not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()