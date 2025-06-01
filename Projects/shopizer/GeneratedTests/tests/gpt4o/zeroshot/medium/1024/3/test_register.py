import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookie_button.click()

        # Click account button and select "Register"
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in the registration form
        email = self.generate_random_email()
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("test**11")
        wait.until(EC.presence_of_element_located((By.NAME, "repeatPassword"))).send_keys("test**11")
        wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Test")
        wait.until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("User")

        # Select country and state
        country_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='country']")))
        country_dropdown.click()
        country_dropdown.send_keys("Canada" + Keys.ENTER)

        state_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='state']")))
        state_dropdown.click()
        state_dropdown.send_keys("Quebec" + Keys.ENTER)

        # Submit the registration form
        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']")))
        register_button.click()

        # Wait for redirect and confirm success
        wait.until(EC.url_contains("/my-account"))

        current_url = driver.current_url
        if not "/my-account" in current_url:
            self.fail("Failure: Did not redirect to /my-account, current URL: " + current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()