from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"
    
    def test_user_registration(self):
        driver = self.driver
        
        # Accept cookies
        accept_cookies_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_btn.click()

        # Open registration page
        account_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in registration form
        email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_field.send_keys(self.random_email())

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("test**11")
        
        repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_field.send_keys("test**11")
        
        first_name_field = driver.find_element(By.NAME, "firstName")
        first_name_field.send_keys("Test")
        
        last_name_field = driver.find_element(By.NAME, "lastName")
        last_name_field.send_keys("User")
        
        # Select country and state
        country_select = driver.find_element(By.TAG_NAME, "select")
        country_select.click()
        country_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Canada']")))
        country_option.click()
        
        state_select = driver.find_element(By.XPATH, "//select[contains(@class,'login-input')][last()]")
        state_select.click()
        state_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Quebec']")))
        state_option.click()

        # Submit the form
        register_button = driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        register_button.click()

        # Check for redirect to "/my-account"
        try:
            self.wait.until(EC.url_contains("/my-account"))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url)
        except Exception as e:
            self.fail(f"Registration failed or did not redirect properly, current URL: {driver.current_url}")

if __name__ == "__main__":
    unittest.main()