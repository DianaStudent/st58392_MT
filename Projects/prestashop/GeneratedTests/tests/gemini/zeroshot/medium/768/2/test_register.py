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
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8080/en/"
        self.email = f"test_{random.randint(100000, 999999)}@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Click on the login link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 2. Click on the register link on the login page
        try:
            create_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
            )
            create_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click create account link: {e}")

        # 3. Fill in the registration form
        try:
            # Select gender
            mr_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Fill in first name
            firstname_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")

            # Fill in last name
            lastname_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")

            # Fill in email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(self.email)

            # Fill in password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys(self.password)

            # Fill in birthday
            birthday_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            )
            birthday_input.send_keys("01/01/2000")

            # Check required checkboxes
            psgdpr_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            customer_privacy_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

        except Exception as e:
            self.fail(f"Could not fill in registration form: {e}")

        # 4. Submit the form
        try:
            save_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Save')]"))
            )
            save_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # 5. Confirm success by checking for the presence of "Sign out"
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout') and contains(text(), 'Sign out')]"))
            )
            self.assertIsNotNone(sign_out_link, "Sign out link not found")
            self.assertNotEqual(sign_out_link.text, "", "Sign out link text is empty")
            self.assertEqual(sign_out_link.text, "Sign out", "Incorrect text: " + sign_out_link.text)

        except Exception as e:
            self.fail(f"Registration failed: {e}")

if __name__ == "__main__":
    unittest.main()