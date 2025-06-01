from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        # Setup Chrome and the driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies if button is present
        cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        if cookie_button:
            cookie_button.click()

        # Click on the account button and select "Register"
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active")))
        if not account_button:
            self.fail("Account button not found")
        account_button.click()

        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        if not register_link:
            self.fail("Register link not found")
        register_link.click()

        # Fill in the registration form
        dynamic_email = f"test_user_{random.randint(1000,9999)}@example.com"
        wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(dynamic_email)
        wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys("test**11")
        wait.until(EC.element_to_be_clickable((By.NAME, "repeatPassword"))).send_keys("test**11")
        wait.until(EC.element_to_be_clickable((By.NAME, "firstName"))).send_keys("Test")
        wait.until(EC.element_to_be_clickable((By.NAME, "lastName"))).send_keys("User")

        # Select a country and a region/state
        country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='country']")))
        if not country_select:
            self.fail("Country select not found")
        country_select.click()
        country_options = country_select.find_elements(By.TAG_NAME, 'option')
        for option in country_options:
            if option.text == "Canada":
                option.click()
                break

        state_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='state']")))
        if not state_select:
            self.fail("State select not found")
        state_select.click()
        state_options = state_select.find_elements(By.TAG_NAME, 'option')
        for option in state_options:
            if option.text == "Quebec":
                option.click()
                break

        # Submit the registration form
        register_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        if not register_button:
            self.fail("Register button not found")
        register_button.click()

        # Confirm success by checking if the current URL includes "/my-account"
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Registration did not redirect to '/my-account'")
        else:
            self.assertIn("/my-account", driver.current_url)

if __name__ == "__main__":
    unittest.main()