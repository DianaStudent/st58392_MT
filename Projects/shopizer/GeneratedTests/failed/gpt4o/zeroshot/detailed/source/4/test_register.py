from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def generate_email(self):
        random_string = str(random.randint(100000, 999999))
        return f"test_{random_string}@user.com"
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the home page and accept cookies if present
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies_button.click()
        except:
            pass

        # Step 2: Click on the account icon/button
        account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'account-setting-active')))
        account_button.click()

        # Step 3: Select the "Register" option
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register')))
        register_link.click()

        # Step 4: Wait for the registration page to load
        # Step 5: Fill in all fields: email, password, repeat password, first name, last name
        email = self.generate_email()
        wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(email)
        wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys('test**11')
        wait.until(EC.element_to_be_clickable((By.NAME, 'repeatPassword'))).send_keys('test**11')
        wait.until(EC.element_to_be_clickable((By.NAME, 'firstName'))).send_keys('Test')
        wait.until(EC.element_to_be_clickable((By.NAME, 'lastName'))).send_keys('User')
        
        # Step 6: Select a first country from the dropdown and wait for region/state dropdown to load
        country_dropdown = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'select')))
        country_dropdown.click()
        country_dropdown.find_elements(By.TAG_NAME, 'option')[1].click()
        
        # Step 7: Select a first state after selecting a country
        state_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@data-name="state"]')))
        state_dropdown.click()
        state_dropdown.find_elements(By.TAG_NAME, 'option')[1].click()
        
        # Step 8: Submit the form
        register_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        register_button.click()

        # Step 9: Wait for redirection and confirm registration success
        wait.until(EC.url_contains("/my-account"))
        if "/my-account" not in driver.current_url:
            self.fail("Registration unsuccessful, did not redirect to /my-account")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()