import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # Wait for and accept cookies
        self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button"))).click()

        # Click on the account icon/button
        account_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_button.click()

        # Click on the "Register" link
        register_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # Wait for the registration page to load
        self.wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Generate a random email
        random_email = f"test_{self.generate_random_string(6)}@user.com"

        # Fill in registration fields
        driver.find_element(By.NAME, "email").send_keys(random_email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Select the first country
        country_select = driver.find_element(By.CSS_SELECTOR, "select[name='country']")
        first_country_option = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "option"))
        )
        first_country_option.click()

        # Wait for state dropdown to update
        state_select = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "select[name='state']")
        ))
        
        # Select the first state
        first_state_option = state_select.find_element(By.TAG_NAME, "option")
        first_state_option.click()

        # Click outside to ensure the dropdown selections are processed
        driver.find_element(By.TAG_NAME, "body").click()

        # Submit the registration form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait for redirection and verify the current URL
        self.wait.until(lambda d: "/my-account" in d.current_url)

        # Check if registration was successful by confirming redirection
        if "/my-account" not in driver.current_url:
            self.fail("Registration failed or did not redirect to account page.")

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

if __name__ == "__main__":
    unittest.main()