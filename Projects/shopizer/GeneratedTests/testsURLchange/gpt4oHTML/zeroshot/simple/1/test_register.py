import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome WebDriver using WebDriver Manager
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the home page
        driver.get("http://localhost/")  # Adjust the URL for your testing environment

        # Accept cookies if the button is present
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found: {str(e)}")

        # Click on the "Register" link
        try:
            register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except Exception as e:
            self.fail(f"Register link not found: {str(e)}")

        # Generate a dynamic email for registration
        email = f"test_{int(time.time())}@example.com"

        # Fill in the registration form
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_input.send_keys(email)

            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")

            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")

            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")

            country_select = driver.find_element(By.XPATH, "//select[contains(., 'Select a country')]/option[@value='CA']")
            country_select.click()

            state_select = driver.find_element(By.XPATH, "//select[contains(., 'Select a state')]/option[@value='QC']")
            state_select.click()

            register_button = driver.find_element(By.XPATH, "//button/span[text()='Register']")
            register_button.click()

        except Exception as e:
            self.fail(f"Error filling registration form: {str(e)}")

        # Verify that the URL contains '/my-account' after registration
        try:
            wait.until(lambda d: re.search(r"/my-account", d.current_url))
        except Exception as e:
            self.fail(f"Did not redirect to /my-account page: {str(e)}")

    def tearDown(self):
        # Quit the browser after test execution
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()