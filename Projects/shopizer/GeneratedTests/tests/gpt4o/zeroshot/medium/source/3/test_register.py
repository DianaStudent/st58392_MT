import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # 1. Open the home page.
        driver.get("http://localhost/")
        
        # Accept cookies
        try:
            accept_cookies_btn = wait.until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            )
            accept_cookies_btn.click()
        except:
            self.fail("Accept cookies button not found.")
        
        # 2. Click on the account button and then select "Register".
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.account-setting-active'))
            )
            account_button.click()
        except:
            self.fail("Account button not found.")
        
        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Register'))
            )
            register_link.click()
        except:
            self.fail("Register link not found.")
        
        # 3. Fill in the registration form.
        email = f"test_{random.randint(1000, 9999)}@user.com"
        
        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
            email_input.send_keys(email)
        except:
            self.fail("Email input not found.")
        
        try:
            password_input = driver.find_element(By.NAME, 'password')
            password_input.send_keys("test**11")
        except:
            self.fail("Password input not found.")
        
        try:
            repeat_password_input = driver.find_element(By.NAME, 'repeatPassword')
            repeat_password_input.send_keys("test**11")
        except:
            self.fail("Repeat password input not found.")
        
        try:
            first_name_input = driver.find_element(By.NAME, 'firstName')
            first_name_input.send_keys("Test")
        except:
            self.fail("First name input not found.")
        
        try:
            last_name_input = driver.find_element(By.NAME, 'lastName')
            last_name_input.send_keys("User")
        except:
            self.fail("Last name input not found.")
        
        # 4. Select a country and a region/state.
        try:
            country_select = driver.find_element(By.XPATH, "//select/option[text()='Canada']")
            country_select.click()
        except:
            self.fail("Country select option not found.")
        
        try:
            state_select = driver.find_element(By.XPATH, "//select/option[text()='Quebec']")
            state_select.click()
        except:
            self.fail("State select option not found.")
        
        # 5. Submit the registration form.
        try:
            register_button = driver.find_element(By.XPATH, "//button/span[text()='Register']")
            register_button.click()
        except:
            self.fail("Register button not found.")
        
        # 6. Wait for redirect and confirm success by checking the URL.
        try:
            wait.until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Registration failed to redirect to /my-account.")

if __name__ == "__main__":
    unittest.main()