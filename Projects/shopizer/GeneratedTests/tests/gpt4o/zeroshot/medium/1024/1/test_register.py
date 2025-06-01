from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def generate_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@mail.com"

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        accept_cookies_button = wait.until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        accept_cookies_button.click()

        # Open register page
        account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_button.click()

        register_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        register_link.click()

        # Wait for the registration form
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill in registration form
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys(self.generate_email())

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("test**11")

        repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_input.send_keys("test**11")

        first_name_input = driver.find_element(By.NAME, "firstName")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.NAME, "lastName")
        last_name_input.send_keys("User")

        # Select country
        country_select = driver.find_element(By.CSS_SELECTOR, "select[name='country']")
        country_select.send_keys("Canada")
        country_select.send_keys(Keys.TAB)

        # Select state
        state_select = driver.find_element(By.CSS_SELECTOR, "select[name='state']")
        state_select.send_keys("Quebec")
        state_select.send_keys(Keys.TAB)

        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()

        # Verify successful registration by URL
        try:
            success_url = wait.until(EC.url_contains("/my-account"))
            self.assertTrue(success_url)
        except TimeoutError:
            self.fail("Registration was not successful, '/my-account' not found in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()