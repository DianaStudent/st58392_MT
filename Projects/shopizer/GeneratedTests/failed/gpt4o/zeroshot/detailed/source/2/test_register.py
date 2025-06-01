from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Accept the cookies
        wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))).click()

        # Open account settings
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()

        # Select Register option
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for registration form
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill in registration form
        email = self.generate_email()
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Select a country and state
        country_select = driver.find_element(By.CSS_SELECTOR, "select:nth-of-type(1)")
        country_select.click()
        country_select.send_keys(Keys.ARROW_DOWN + Keys.RETURN)

        # Wait for state dropdown and select state
        state_select = driver.find_element(By.CSS_SELECTOR, "select:nth-of-type(2)")
        state_select.click()
        state_select.send_keys(Keys.ARROW_DOWN + Keys.RETURN)

        # Submit form
        submit_button = driver.find_element(By.CSS_SELECTOR, ".button-box button")
        submit_button.click()

        # Confirm registration success by URL
        wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url

        self.assertIn("/my-account", current_url, "Registration failed or did not redirect to /my-account.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()