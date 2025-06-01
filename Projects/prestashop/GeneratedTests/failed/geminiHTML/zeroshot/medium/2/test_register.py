from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the login link in the top menu.
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(text(), 'Sign in')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. Click on the register link on the login page.
        try:
            create_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            create_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click create account link: {e}")

        # 4. Fill in the registration form fields:
        #    - Gender, First name, Last name, Email, Password, Birthday

        # Generate a random email
        email_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = f"test_{email_prefix}@user.com"
        password = "test@user1"

        try:
            # Gender
            mr_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # First name
            firstname_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")

            # Last name
            lastname_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")

            # Email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(email)

            # Password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys(password)

            # Birthday
            birthday_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            )
            birthday_input.send_keys("01/01/1990")

        except Exception as e:
            self.fail(f"Could not fill in form fields: {e}")

        # 5. Check required checkboxes.
        try:
            # GDPR agreement
            psgdpr_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            # Customer privacy
            customer_privacy_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

        except Exception as e:
            self.fail(f"Could not check required checkboxes: {e}")

        # 6. Submit the form.
        try:
            save_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
            )
            save_button.click()
        except Exception as e:
            self.fail(f"Could not submit the form: {e}")

        # 7. Confirm success by checking for the presence of "Sign out" in the top bar.
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(text(), 'Sign out')]"))
            )
            self.assertIsNotNone(sign_out_link.text)
            self.assertEqual(sign_out_link.text, "Sign out")

        except Exception as e:
            self.fail(f"Registration failed: Could not find 'Sign out' link: {e}")

if __name__ == "__main__":
    unittest.main()