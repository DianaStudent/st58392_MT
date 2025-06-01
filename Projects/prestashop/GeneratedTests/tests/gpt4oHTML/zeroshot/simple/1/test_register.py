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

class TestRegistrationProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def generate_random_email(self):
        domains = ["example.com", "test.com", "mail.com"]
        letters = string.ascii_lowercase
        random_username = ''.join(random.choice(letters) for i in range(8))
        random_domain = random.choice(domains)
        return f"{random_username}@{random_domain}"

    def test_register_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Click "Create account" link from the footer
            create_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create account")))
            create_account_link.click()

            # Fill in the registration form
            email = self.generate_random_email()
            password = "test@user1"
            
            # Wait and fill first name
            firstname_field = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
            firstname_field.send_keys("TestFirstName")

            # Wait and fill last name
            lastname_field = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
            lastname_field.send_keys("TestLastName")
            
            # Wait and fill email
            email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
            email_field.send_keys(email)
            
            # Wait and fill password
            password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
            password_field.send_keys(password)

            # Check all required checkboxes
            checkboxes = [
                ("optin", "Receive offers from our partners"),
                ("psgdpr", "I agree to the terms and conditions and the privacy policy"),
                ("newsletter", "Sign up for our newsletter"),
                ("customer_privacy", "Customer data privacy")
            ]
            for checkbox_name, label_text in checkboxes:
                checkbox_label = driver.find_element(By.XPATH, f"//label[contains(., '{label_text}')]//input")
                if not checkbox_label.is_selected():
                    checkbox_label.click()
            
            # Submit the registration form
            save_button = driver.find_element(By.CLASS_NAME, "form-control-submit")
            save_button.click()
            
            # Confirm success: Check that "Sign out" link appears
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign out")))
        
        except Exception as e:
            self.fail(f"Test failed due to missing element or timeout: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()