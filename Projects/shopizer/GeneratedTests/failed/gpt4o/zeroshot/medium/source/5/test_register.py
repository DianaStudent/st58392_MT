from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_user_registration(self):
        # Accept cookies
        try:
            accept_cookies = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            accept_cookies.click()
        except:
            self.fail('Cookie consent button not found.')

        # Open Register Page
        try:
            account_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_btn.click()
            register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register')))
            register_link.click()
        except:
            self.fail('Registration link/button not found.')

        # Fill Registration Form
        try:
            email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
            email_input.send_keys(f'test_user_{int(time.time())}@example.com')
            
            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.send_keys('test**11')
            
            repeat_password_input = self.driver.find_element(By.NAME, 'repeatPassword')
            repeat_password_input.send_keys('test**11')
            
            first_name_input = self.driver.find_element(By.NAME, 'firstName')
            first_name_input.send_keys('Test')
            
            last_name_input = self.driver.find_element(By.NAME, 'lastName')
            last_name_input.send_keys('User')
            
            country_select = self.driver.find_element(By.CSS_SELECTOR, 'select[name="country"]')
            country_select.click()
            country_select.send_keys('Canada')
            country_select.send_keys(Keys.ENTER)
            
            state_select = self.driver.find_element(By.CSS_SELECTOR, 'select[name="state"]')
            state_select.click()
            state_select.send_keys('Quebec')
            state_select.send_keys(Keys.ENTER)
        except:
            self.fail('Form elements not found or could not be interacted with.')

        # Submit Registration Form
        try:
            submit_btn = self.driver.find_element(By.XPATH, '//button/span[text()="Register"]/..')
            submit_btn.click()
        except:
            self.fail('Register button not found.')

        # Verify Account Creation
        try:
            self.wait.until(EC.url_contains("/my-account"))
            current_url = self.driver.current_url
            self.assertIn("/my-account", current_url)
        except:
            self.fail('Redirect to /my-account failed.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()