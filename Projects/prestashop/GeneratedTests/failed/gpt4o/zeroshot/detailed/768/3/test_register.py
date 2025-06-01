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

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the homepage
        wait.until(EC.presence_of_element_located((By.ID, 'index')))
        
        # Step 2: Click the login link from the top navigation
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="/en/login"]')))
        sign_in_button.click()

        # Step 3: On the login page, click on the register link (e.g. "No account? Create one here")
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()
        
        # Step 4: Fill in the registration form
        wait.until(EC.presence_of_element_located((By.ID, 'customer-form')))
        
        driver.find_element(By.ID, 'field-id_gender-1').click()
        
        driver.find_element(By.ID, 'field-firstname').send_keys("Test")
        driver.find_element(By.ID, 'field-lastname').send_keys("User")
        
        # Generate a dynamic email
        email = f"test_{random.randint(100000, 999999)}@user.com"
        driver.find_element(By.ID, 'field-email').send_keys(email)
        
        driver.find_element(By.ID, 'field-password').send_keys("test@user1")
        driver.find_element(By.ID, 'field-birthday').send_keys("01/01/2000")
        
        # Tick checkboxes
        checkboxes = [
            'field-optin', 
            'field-newsletter', 
            'field-psgdpr', 
            'field-customer_privacy'
        ]
        
        for checkbox in checkboxes:
            driver.find_element(By.NAME, checkbox).click()
        
        # Step 5: Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        save_button.click()
        
        # Step 6: Wait for the redirect after login
        wait.until(EC.presence_of_element_located((By.ID, 'index')))
        
        # Step 7: Confirm that login was successful
        try:
            sign_out_button = driver.find_element(By.LINK_TEXT, "Sign out")
        except:
            self.fail("Sign out button not present, registration might not be successful.")
        
        username_display = driver.find_element(By.CSS_SELECTOR, 'a[href*="/my-account"] span.hidden-sm-down')
        self.assertTrue(username_display.is_displayed(), "Username is not displayed, registration might not be successful.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()