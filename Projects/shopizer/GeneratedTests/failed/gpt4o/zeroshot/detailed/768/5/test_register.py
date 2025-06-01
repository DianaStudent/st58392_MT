from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        
        # Accept cookies
        self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))).click()

        # Click on account icon
        account_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        # Click on "Register"
        register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in registration form
        email = f"test_{int(time.time())}@user.com"
        self.wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        self.wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys("test**11")
        self.wait.until(EC.element_to_be_clickable((By.NAME, "repeatPassword"))).send_keys("test**11")
        self.wait.until(EC.element_to_be_clickable((By.NAME, "firstName"))).send_keys("Test")
        self.wait.until(EC.element_to_be_clickable((By.NAME, "lastName"))).send_keys("User")

        # Select a country
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='country'] > option[value='CA']"))).click()

        # Ensure state selector is populated and select a state
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='stateProvince']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='stateProvince'] > option[value='QC']"))).click()

        # Submit the registration form
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']"))).click()

        # Verify the registration was successful
        self.wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()