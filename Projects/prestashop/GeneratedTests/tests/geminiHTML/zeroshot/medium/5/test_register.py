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
        self.driver.implicitly_wait(10)
        self.email = 'test_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + '@user.com'
        self.password = 'test@user1'

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the login link in the top menu.
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. Click on the register link on the login page.
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click register link: {e}")

        # 4. Fill in the registration form fields:
        #    - Gender, First name, Last name, Email, Password, Birthday
        try:
            # Gender
            mr_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # First name
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            first_name_field.send_keys("Test")

            # Last name
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            last_name_field.send_keys("User")

            # Email
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_field.send_keys(self.email)

            # Password
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_field.send_keys(self.password)

            # Birthday (Optional)
            birthday_field = driver.find_element(By.ID, "field-birthday")
            birthday_field.send_keys("01/01/1990")

        except Exception as e:
            self.fail(f"Could not fill in form fields: {e}")

        # 5. Check required checkboxes.
        try:
            # GDPR agreement
            gdpr_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            gdpr_checkbox.click()

            # Customer Privacy
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
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertIsNotNone(sign_out_link, "Sign out link not found after registration.")
        except Exception as e:
            self.fail(f"Registration failed: {e}")

if __name__ == "__main__":
    unittest.main()