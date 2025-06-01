import unittest
import random
import string

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

        # 1. Click on the login link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 2. Click on the registration link
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click register link: {e}")

        # 3. Fill in the registration form
        email = "test_" + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + "@user.com"
        password = "test@user1"

        try:
            # Select gender
            mr_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Fill first name
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            first_name_field.send_keys("Test")

            # Fill last name
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            last_name_field.send_keys("User")

            # Fill email
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_field.send_keys(email)

            # Fill password
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_field.send_keys(password)

            # Fill birthday
            birthday_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            )
            birthday_field.send_keys("01/01/2000")

            # Check required checkboxes
            psgdpr_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            customer_privacy_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

            # Submit the form
            save_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'form-control-submit')]"))
            )
            save_button.click()

        except Exception as e:
            self.fail(f"Could not fill or submit form: {e}")

        # 4. Confirm success by checking for the presence of "Sign out"
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
            )
            self.assertIsNotNone(sign_out_link.text)
            self.assertNotEqual(sign_out_link.text, "")
            self.assertEqual(sign_out_link.text.strip(), "Sign out")

        except Exception as e:
            self.fail(f"Could not find sign out link: {e}")


if __name__ == "__main__":
    unittest.main()