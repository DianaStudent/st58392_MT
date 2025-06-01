import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string


class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to login page
        sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Navigate to registration page
        create_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        create_account_link.click()

        # Fill the registration form
        # Social title
        mr_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#field-id_gender-1")))
        mr_radio.click()

        # First name
        firstname_input = driver.find_element(By.CSS_SELECTOR, "input#field-firstname")
        firstname_input.send_keys("Test")

        # Last name
        lastname_input = driver.find_element(By.CSS_SELECTOR, "input#field-lastname")
        lastname_input.send_keys("User")

        # Email
        email_input = driver.find_element(By.CSS_SELECTOR, "input#field-email")
        random_email = "test_" + ''.join(random.choices(string.ascii_lowercase, k=5)) + "@mail.com"
        email_input.send_keys(random_email)

        # Password
        password_input = driver.find_element(By.CSS_SELECTOR, "input#field-password")
        password_input.send_keys("test@user1")

        # Opt-in for offers
        optin_checkbox = driver.find_element(By.NAME, "optin")
        optin_checkbox.click()

        # Agree to terms and conditions
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        # Sign up for newsletter
        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        newsletter_checkbox.click()

        # Agree to customer privacy
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        # Submit the form
        save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'].form-control-submit")
        save_button.click()

        # Confirm success by checking "Sign out"
        try:
            sign_out_element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign out")))
        except:
            self.fail("Registration failed: 'Sign out' not found, registration process failed to complete successfully.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()