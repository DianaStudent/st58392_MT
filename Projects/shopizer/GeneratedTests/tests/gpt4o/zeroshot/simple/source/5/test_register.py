import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def generate_random_email(self):
        # Generates a random email for testing
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"

    def test_register_user(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookies acceptance button not found or clickable.")

        # Navigate to register page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_button.click()
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link not found or clickable.")
        
        # Fill out the registration form
        email = self.generate_random_email()
        password = "test**11"
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(password)
            repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
            repeat_password_field.send_keys(password)

            first_name_field = driver.find_element(By.NAME, "firstName")
            first_name_field.send_keys("Test")
            last_name_field = driver.find_element(By.NAME, "lastName")
            last_name_field.send_keys("User")
            
            country_select = driver.find_element(By.CSS_SELECTOR, "select[name='country']")
            country_select.send_keys("Canada")
            state_select = driver.find_element(By.CSS_SELECTOR, "select[name='state']")
            state_select.send_keys("Quebec")
            
            register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            register_button.click()
        except:
            self.fail("Registration form could not be filled or submitted.")
        
        # Confirm success: Check if redirected to the my-account page
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
        except:
            self.fail("Did not redirect to the /my-account page after registration.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()