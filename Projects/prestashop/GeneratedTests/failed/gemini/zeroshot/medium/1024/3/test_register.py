from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

        # 1. Click on the login link
        try:
            sign_in_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not click sign-in link: {e}")

        # 2. Click on the register link on the login page
        try:
            register_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not click register link: {e}")

        # 3. Fill in the registration form
        email = f"test_{random.randint(100000, 999999)}@user.com"
        password = "test@user1"

        try:
            # Select gender
            mr_radio = wait.until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Fill in first name
            first_name_field = wait.until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            first_name_field.send_keys("Test")

            # Fill in last name
            last_name_field = wait.until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            last_name_field.send_keys("User")

            # Fill in email
            email_field = wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_field.send_keys(email)

            # Fill in password
            password_field = wait.until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_field.send_keys(password)

            # Fill in birthday
            birthday_field = wait.until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            )
            birthday_field.send_keys("01/01/1990")

            # Check required checkboxes
            psgdpr_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            customer_privacy_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

        except Exception as e:
            self.fail(f"Could not fill form fields: {e}")

        # 4. Submit the form
        try:
            save_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
            )
            save_button.click()
        except Exception as e:
            self.fail(f"Could not submit the form: {e}")

        # 5. Confirm success by checking for the presence of "Sign out" in the top bar
        try:
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
            )
            self.assertIsNotNone(sign_out_link, "Sign out link not found")
            self.assertEqual("Sign out", sign_out_link.text)

        except Exception as e:
            self.fail(f"Registration failed: {e}")

if __name__ == "__main__":
    unittest.main()