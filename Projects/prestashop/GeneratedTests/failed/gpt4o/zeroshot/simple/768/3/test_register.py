from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_registration_process(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to the registration page
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            login_link.click()
            
            create_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
            create_account_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to registration page: {e}")

        # Fill in the registration form
        try:
            # Select Gender
            driver.find_element(By.ID, "field-id_gender-1").click()

            # Fill in First Name
            driver.find_element(By.ID, "field-firstname").send_keys("Test")

            # Fill in Last Name
            driver.find_element(By.ID, "field-lastname").send_keys("User")

            # Generate and fill in Email
            random_email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"
            driver.find_element(By.ID, "field-email").send_keys(random_email)

            # Fill in Password
            driver.find_element(By.ID, "field-password").send_keys("test@user1")

            # Agree to terms (check checkboxes)
            driver.find_element(By.NAME, "psgdpr").click()
            driver.find_element(By.NAME, "customer_privacy").click()
            
            # Check optional checkboxes
            driver.find_element(By.NAME, "optin").click()
            driver.find_element(By.NAME, "newsletter").click()

            # Submit the form
            driver.find_element(By.CSS_SELECTOR, "button.form-control-submit").click()
        except Exception as e:
            self.fail(f"Failed to fill registration form: {e}")
        
        # Confirm success
        try:
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign out")))
        except Exception as e:
            self.fail("Registration did not succeed: 'Sign out' link not found.")

if __name__ == "__main__":
    unittest.main()