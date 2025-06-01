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
        except Exception as e:
            self.fail(f"Could not find or click Sign in link: {e}")

        # 2. Go to registration page
        try:
            create_account_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            create_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click Create account link: {e}")

        # 3. Fill registration form
        email = f"test{random.randint(1000, 9999)}@user.com"
        password = "test@user1"

        try:
            # Select social title
            mr_radio = wait.until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Fill first name
            firstname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")

            # Fill last name
            lastname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")

            # Fill email
            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(email)

            # Fill password
            password_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys(password)

            # Select all checkboxes
            psgdpr_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            newsletter_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "newsletter"))
            )
            newsletter_checkbox.click()

            customer_privacy_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

        except Exception as e:
            self.fail(f"Could not fill registration form: {e}")

        # 4. Submit registration form
        try:
            save_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
            )
            save_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # 5. Verify successful registration
        try:
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue("Sign out" in sign_out_link.text)
        except Exception as e:
            self.fail(f"Registration failed: {e}")

if __name__ == "__main__":
    unittest.main()