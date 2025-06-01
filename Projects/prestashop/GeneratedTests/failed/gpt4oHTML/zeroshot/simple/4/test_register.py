from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")  # Start from the home page

    def generate_random_email(self):
        domain = "@example.com"
        random_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return random_prefix + domain

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the registration page
        try:
            create_account_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Create account']")))
            create_account_link.click()
        except Exception as e:
            self.fail("Create account link not found: " + str(e))

        # Fill out the registration form
        try:
            # Select Social Title
            mr_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Mr.')]//input[@name='id_gender']")))
            mr_radio.click()

            # Fill Firstname
            firstname_field = wait.until(EC.element_to_be_clickable((By.ID, "field-firstname")))
            firstname_field.send_keys("Test")

            # Fill Lastname
            lastname_field = driver.find_element(By.ID, "field-lastname")
            lastname_field.send_keys("User")

            # Fill Email
            email_field = driver.find_element(By.ID, "field-email")
            email_field.send_keys(self.generate_random_email())

            # Fill Password
            password_field = driver.find_element(By.ID, "field-password")
            password_field.send_keys("test@user1")

            # Agree to terms and privacy policy
            terms_checkbox = driver.find_element(By.XPATH, "//input[@name='psgdpr']")
            terms_checkbox.click()

            # Agree to customer data privacy
            privacy_checkbox = driver.find_element(By.XPATH, "//input[@name='customer_privacy']")
            privacy_checkbox.click()

            # Submit form
            save_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Save')]")
            save_button.click()
        except Exception as e:
            self.fail("Registration form interaction failed: " + str(e))

        # Confirm registration success by checking for "Sign out" text
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='logout' and contains(text(),'Sign out')]")))
        except Exception as e:
            self.fail("Registration not successful, 'Sign out' not found: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()