from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver
        wait = self.wait

        # Helper function to generate a random email
        def generate_random_email():
            return "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"

        random_email = generate_random_email()

        # Accept cookies
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except:
            self.fail("Could not find the 'Accept cookies' button.")

        # Click on the account icon/button
        try:
            account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            account_icon.click()
        except:
            self.fail("Could not find the account icon/button.")

        # Click on "Register"
        try:
            register_btn = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_btn.click()
        except:
            self.fail("Could not find the 'Register' link.")

        # Wait for registration form to load
        time.sleep(2)  # Sometimes a short sleep is necessary for animations to complete

        # Fill in registration form
        try:
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_input.send_keys(random_email)

            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("test**11")

            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_input.send_keys("test**11")

            first_name_input = driver.find_element(By.NAME, "firstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")
        except:
            self.fail("Could not find one or more input fields on the registration form.")

        # Select country and state
        try:
            country_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select option[value='CA']")))
            country_dropdown.click()

            # Ensure country selector dropdown closes
            first_name_input.click()

            state_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select + select option[value='QC']")))
            state_dropdown.click()
        except:
            self.fail("Could not select country or state from the dropdown.")

        # Submit form
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']")))
            register_button.click()
        except:
            self.fail("Could not find the 'Register' button.")

        # Verify redirection to My Account page
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertTrue("/my-account" in driver.current_url, "Registration did not redirect to My Account page.")
        except:
            self.fail("Failed to verify redirection to My Account page after registration.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()