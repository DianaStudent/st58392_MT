from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        
        # Step 1. Click on the login link
        login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in')))
        login_link.click()

        # Step 2. Click on the register link
        register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Create one here')))
        register_link.click()

        # Step 3. Fill in the registration form
        # Gender
        gender_radio_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'field-id_gender-1')))
        gender_radio_button.click()

        # First name
        first_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'field-firstname')))
        first_name_input.send_keys('Test')

        # Last name
        last_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'field-lastname')))
        last_name_input.send_keys('User')

        # Email
        email_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'field-email')))
        email_input.send_keys(f'test_{int(time.time())}@user.com')

        # Password
        password_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'field-password')))
        password_input.send_keys('test@user1')

        # Birthday
        birthday_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'field-birthday')))
        birthday_input.send_keys('05/31/1970')

        # Check required checkboxes
        psgdpr_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, 'psgdpr')))
        psgdpr_checkbox.click()

        customer_privacy_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, 'customer_privacy')))
        customer_privacy_checkbox.click()

        # Submit the form
        save_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary.form-control-submit')))
        save_button.click()

        # Step 4. Confirm success
        sign_out_text = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign out')))
        if not sign_out_text or not sign_out_text.is_displayed():
            self.fail("Sign out link not found; registration likely failed.")

if __name__ == "__main__":
    unittest.main()