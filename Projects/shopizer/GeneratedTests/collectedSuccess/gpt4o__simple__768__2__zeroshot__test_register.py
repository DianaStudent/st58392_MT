from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Accept cookies
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookies acceptance button not found or clickable: {str(e)}")
        
        try:
            # Navigate to the registration page
            account_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_button.click()

            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Navigation to registration page failed: {str(e)}")

        try:
            # Fill the registration form
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email = f"test_{random.randint(1000, 9999)}@user.com"
            email_field.send_keys(email)

            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys("test**11")

            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_field.send_keys("test**11")

            first_name_field = driver.find_element(By.NAME, "firstName")
            first_name_field.send_keys("Test")

            last_name_field = driver.find_element(By.NAME, "lastName")
            last_name_field.send_keys("User")

            country_dropdown = driver.find_element(By.XPATH, "//select/option[contains(text(), 'Canada')]")
            country_dropdown.click()

            state_dropdown = driver.find_element(By.XPATH, "//select/option[contains(text(), 'Quebec')]")
            state_dropdown.click()

            register_button = driver.find_element(By.XPATH, "//button/span[text()='Register']")
            register_button.click()
        except Exception as e:
            self.fail(f"Registration form filling or submission failed: {str(e)}")

        try:
            # Verify successful registration
            wait.until(EC.url_contains("/my-account"))
            print("Registration successful. Redirected to My Account page.")
        except Exception as e:
            self.fail(f"Registration success verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()