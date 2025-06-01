import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Go to Sign in page
        try:
            sign_in_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a"))
            )
            sign_in_link.click()
        except:
            self.fail("Could not find 'Sign in' link on the home page.")

        # 2. Go to registration page
        try:
            create_account_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            create_account_link.click()
        except:
            self.fail("Could not find 'Create account' link on the login page.")

        # 3. Fill registration form
        email = f"test{random.randint(1000, 9999)}@user.com"
        password = "test@user1"

        try:
            # Select social title
            mr_radio = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='id_gender' and @value='1']"))
            )
            mr_radio.click()

            # Fill first name
            first_name_field = wait.until(
                EC.visibility_of_element_located((By.ID, "field-firstname"))
            )
            first_name_field.send_keys("Test")

            # Fill last name
            last_name_field = wait.until(
                EC.visibility_of_element_located((By.ID, "field-lastname"))
            )
            last_name_field.send_keys("User")

            # Fill email
            email_field = wait.until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            email_field.send_keys(email)

            # Fill password
            password_field = wait.until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )
            password_field.send_keys(password)

            # Check GDPR checkbox
            gdpr_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            gdpr_checkbox.click()

            # Check Customer privacy checkbox
            customer_privacy_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

            # Check Newsletter checkbox
            newsletter_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "newsletter"))
            )
            newsletter_checkbox.click()

            # Check Optin checkbox
            optin_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "optin"))
            )
            optin_checkbox.click()

        except:
            self.fail("Could not fill the registration form.")

        # 4. Submit registration form
        try:
            save_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'form-control-submit')]"))
            )
            save_button.click()
        except:
            self.fail("Could not submit the registration form.")

        # 5. Verify successful registration
        try:
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out_link.is_displayed())
        except:
            self.fail("Registration failed. 'Sign out' link not found.")

if __name__ == "__main__":
    unittest.main()