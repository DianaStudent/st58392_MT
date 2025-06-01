from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie button not found or not clickable: {str(e)}")

        # Navigate to Register page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
            account_button.click()
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to register page: {str(e)}")

        # Fill registration form
        try:
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            repeat_password_field = wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword")))
            first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            last_name_field = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
            country_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='country']")))
            state_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='state']")))

            email = f"test_{int(time.time())}@example.com"
            email_field.send_keys(email)
            password_field.send_keys("test**11")
            repeat_password_field.send_keys("test**11")
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            country_dropdown.send_keys("Canada")
            state_dropdown.send_keys("Quebec")

            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            submit_button.click()
        except Exception as e:
            self.fail(f"Error filling registration form: {str(e)}")

        # Confirm registration success
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail(f"Registration not successful: Page did not redirect to '/my-account': {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()