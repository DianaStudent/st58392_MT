from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8080/en/"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage (already done in setUp)

        # 2. Click the login link from the top navigation
        try:
            sign_in_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(text(), 'Sign in')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Sign in link not found or not clickable: {e}")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here")
        try:
            create_account_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            create_account_link.click()
        except Exception as e:
            self.fail(f"Create account link not found or not clickable: {e}")

        # 4. Fill in the registration form
        # Generate dynamic email
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(6))
        email = f"test_{random_string}@user.com"

        try:
            # Select Gender
            mr_radio_button = wait.until(
                EC.presence_of_element_located((By.ID, "field-id_gender-1"))
            )
            mr_radio_button.click()

            # Fill First Name
            firstname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")

            # Fill Last Name
            lastname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")

            # Fill Email
            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(email)

            # Fill Password
            password_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys("test@user1")

            # Fill Birthday
            birthday_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            )
            birthday_input.send_keys("01/01/2000")

        except Exception as e:
            self.fail(f"Error filling form fields: {e}")

        # 5. Tick checkboxes
        try:
            # Agree to terms and conditions
            psgdpr_checkbox = wait.until(
                EC.presence_of_element_located((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            # Customer Privacy
            customer_privacy_checkbox = wait.until(
                EC.presence_of_element_located((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

        except Exception as e:
            self.fail(f"Error ticking checkboxes: {e}")

        # 6. Submit the registration form
        try:
            save_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
            )
            save_button.click()
        except Exception as e:
            self.fail(f"Save button not found or not clickable: {e}")

        # 7. Wait for the redirect after login

        # 8. Confirm that login was successful
        try:
            # Check for "Sign out" link
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Sign out')]"))
            )
            self.assertIsNotNone(sign_out_link, "Sign out link is not present")

            # Check for username
            username_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='account']/span[not(@class)]"))
            )
            self.assertIsNotNone(username_element, "Username element is not present")
            self.assertEqual(username_element.text, "Test User", "Username is incorrect")

        except Exception as e:
            self.fail(f"Login confirmation failed: {e}")


if __name__ == "__main__":
    unittest.main()