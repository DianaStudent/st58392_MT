import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@example.com"

    def test_registration(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        # Accept cookies
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))).click()
        except:
            self.fail("Cookie consent button not found or clickable.")

        # Navigate to registration
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()

            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Failed to navigate to registration page.")

        # Fill registration form
        try:
            email = self.generate_random_email()
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)

            driver.find_element(By.NAME, "password").send_keys("test**11")
            driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
            driver.find_element(By.NAME, "firstName").send_keys("Test")
            driver.find_element(By.NAME, "lastName").send_keys("User")
            
            country_select = driver.find_element(By.XPATH, "//select[option[contains(., 'Select a country')]]")
            country_select.click()
            country_select.send_keys("Canada")
            
            state_select = driver.find_element(By.XPATH, "//select[option[contains(., 'Select a state')]]")
            state_select.click()
            state_select.send_keys("Quebec")
            
            driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']").click()
        except:
            self.fail("Failed to fill the registration form.")

        # Confirm success by URL
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url)
        except:
            self.fail("Registration did not succeed or /my-account URL not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()