import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)  # Implicit wait for stabilization
        self.base_url = "http://localhost:8080/en/"
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        driver.get(f"{self.base_url}/en/")
        
        # Navigate to the login page
        user_info = self.wait.until(EC.presence_of_element_located((By.ID, "_desktop_user_info")))
        user_info.find_element(By.LINK_TEXT, "Sign in").click()
        
        # On the login page, click on the register link
        no_account_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        no_account_link.click()
        
        # Fill registration form
        form = self.wait.until(EC.presence_of_element_located((By.ID, "customer-form")))
        
        # Gender
        gender_radio = form.find_element(By.CSS_SELECTOR, "input[name='id_gender'][value='1']")
        driver.execute_script("arguments[0].click();", gender_radio)
        
        # First Name
        firstname_field = form.find_element(By.ID, "field-firstname")
        firstname_field.clear()
        firstname_field.send_keys("Test")
        
        # Last Name
        lastname_field = form.find_element(By.ID, "field-lastname")
        lastname_field.clear()
        lastname_field.send_keys("User")
        
        # Email
        # Generating dynamic email
        email = f"test_{random.randint(100000, 999999)}@user.com"
        email_field = form.find_element(By.ID, "field-email")
        email_field.clear()
        email_field.send_keys(email)
        
        # Password
        password_field = form.find_element(By.ID, "field-password")
        password_field.clear()
        password_field.send_keys("test@user1")
        
        # Birthdate
        birthdate_field = form.find_element(By.ID, "field-birthday")
        birthdate_field.clear()
        birthdate_field.send_keys("01/01/2000")
        
        # Tick checkboxes
        checkboxes = [
            "optin",  # Receive offers
            "psgdpr",  # Agree to terms and conditions
            "newsletter",  # Sign up for newsletter
            "customer_privacy"  # Customer data privacy
        ]
        for checkbox_name in checkboxes:
            checkbox = form.find_element(By.NAME, checkbox_name)
            if not checkbox.is_selected():
                driver.execute_script("arguments[0].click();", checkbox)
        
        # Submit the form
        form.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Wait for redirect and confirm success
        user_info = self.wait.until(EC.presence_of_element_located((By.ID, "_desktop_user_info")))
        
        try:
            # Ensure "Sign out" link is present
            sign_out = user_info.find_element(By.LINK_TEXT, "Sign out")
            self.assertIsNotNone(sign_out, "Sign out link is missing.")
            
            # Ensure the username is displayed
            account_link = user_info.find_element(By.CLASS_NAME, "account")
            account_text = account_link.text.lower()
            self.assertIn("test user", account_text, "Username 'Test User' is not visible.")
        
        except Exception as e:
            self.fail(f"Test failed with exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()