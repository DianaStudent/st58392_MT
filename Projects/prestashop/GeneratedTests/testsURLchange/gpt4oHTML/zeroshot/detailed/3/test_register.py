import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click the login link from the top navigation.
        sign_in_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#_desktop_user_info .user-info a')))
        sign_in_link.click()

        # Step 2: Click on the register link.
        register_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.no-account a[href$="registration"]')))
        register_link.click()

        # Step 3: Fill in the form
        # Gender
        gender_radio = wait.until(EC.presence_of_element_located((By.ID, 'field-id_gender-1')))
        driver.execute_script("arguments[0].click();", gender_radio)
        
        # First name
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, 'field-firstname')))
        first_name_input.send_keys('Test')
        
        # Last name
        last_name_input = wait.until(EC.presence_of_element_located((By.ID, 'field-lastname')))
        last_name_input.send_keys('User')
        
        # Email (dynamically generated)
        random_number = random.randint(100000, 999999)
        email = f'test_{random_number}@user.com'
        email_input = wait.until(EC.presence_of_element_located((By.ID, 'field-email')))
        email_input.send_keys(email)
        
        # Password
        password_input = wait.until(EC.presence_of_element_located((By.ID, 'field-password')))
        password_input.send_keys('test@user1')
        
        # Birthday
        birthday_input = wait.until(EC.presence_of_element_located((By.ID, 'field-birthday')))
        birthday_input.send_keys('01/01/2000')

        # Step 4: Tick checkboxes
        privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, 'customer_privacy')))
        driver.execute_script("arguments[0].click();", privacy_checkbox)

        terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, 'psgdpr')))
        driver.execute_script("arguments[0].click();", terms_checkbox)

        newsletter_checkbox = wait.until(EC.presence_of_element_located((By.NAME, 'newsletter')))
        driver.execute_script("arguments[0].click();", newsletter_checkbox)

        # Step 5: Submit the form
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        submit_button.click()

        # Step 6: Wait and confirm the registration
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout")))

        # Check that "Sign out" is present
        sign_out_button = driver.find_element(By.CSS_SELECTOR, "a.logout")
        self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not displayed")

        # Check that "Test User" is visible
        user_info = driver.find_element(By.CSS_SELECTOR, "a.account span")
        self.assertTrue(user_info.is_displayed() and 'Test User' in user_info.text, "User name is not displayed correctly")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()