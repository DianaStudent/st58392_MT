import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for faster execution
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)
        
    def generate_email(self):
        return "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"

    def test_register_account(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://localhost/")  # Assume the location where the server is running

        # Step 2: Click on the account button and select "Register"
        account_btn_selector = '.account-setting-active'
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, account_btn_selector)))
        driver.find_element(By.CSS_SELECTOR, account_btn_selector).click()

        register_link_selector = '.account-dropdown a[href="/register"]'
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, register_link_selector)))
        driver.find_element(By.CSS_SELECTOR, register_link_selector).click()

        # Step 3: Fill in the registration form
        email = self.generate_email()
        password = "test**11"
        
        self.wait.until(EC.presence_of_element_located((By.NAME, "email")))

        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "repeatPassword").send_keys(password)
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Step 4: Select a country and a region/state
        country_selector = 'select option[value="CA"]'
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, country_selector)))
        driver.find_element(By.CSS_SELECTOR, country_selector).click()

        state_selector = 'select option[value="QC"]'
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, state_selector)))
        driver.find_element(By.CSS_SELECTOR, state_selector).click()

        # Step 5: Submit the registration form
        register_btn_selector = 'div.button-box button[type="submit"]'
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, register_btn_selector)))
        driver.find_element(By.CSS_SELECTOR, register_btn_selector).click()

        # Step 6: Wait for redirect and confirm success by checking if the current URL includes "/my-account"
        self.wait.until(EC.url_contains("/my-account"))
        
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Registration successful and redirected to My Account page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()