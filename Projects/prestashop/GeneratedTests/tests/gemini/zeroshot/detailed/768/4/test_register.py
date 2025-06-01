import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://localhost:8080/en/"
        self.email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        self.credentials = {
            "gender": "1",
            "firstname": "Test",
            "lastname": "User",
            "email": self.email,
            "password": "test@user1",
            "birthday": "01/01/2000"
        }

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Click the login link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 2. Click the registration link
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]"))
            )
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click registration link: {e}")

        # 3. Fill in the registration form
        try:
            # Gender
            gender_radio = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-id_gender-1"))
            )
            gender_radio.click()

            # First name
            firstname_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_field.send_keys(self.credentials["firstname"])

            # Last name
            lastname_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_field.send_keys(self.credentials["lastname"])

            # Email
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_field.send_keys(self.credentials["email"])

            # Password
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_field.send_keys(self.credentials["password"])

            # Birthday
            birthday_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            )
            birthday_field.send_keys(self.credentials["birthday"])
        except Exception as e:
            self.fail(f"Could not fill in form fields: {e}")

        # 4. Tick checkboxes
        try:
            # Privacy checkbox
            privacy_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "customer_privacy"))
            )
            privacy_checkbox.click()

            # Terms and conditions checkbox
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "psgdpr"))
            )
            terms_checkbox.click()

            # Newsletter checkbox
            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "newsletter"))
            )
            newsletter_checkbox.click()
        except Exception as e:
            self.fail(f"Could not tick checkboxes: {e}")

        # 5. Submit the registration form
        try:
            submit_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
            )
            submit_button.click()
        except Exception as e:
            self.fail(f"Could not submit the form: {e}")

        # 6. Wait for redirect and confirm successful login
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
        except Exception as e:
            self.fail(f"Registration or login failed: {e}")

        # 7. Confirm "Sign out" button is present
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertIsNotNone(sign_out_link.text)
            self.assertEqual(sign_out_link.text, "Sign out")
        except Exception as e:
            self.fail(f"Sign out link not found or empty: {e}")

        # 8. Confirm username is visible
        try:
            username_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[@class='account']/span"))
            )
            self.assertIsNotNone(username_element.text)
            expected_username = self.credentials["firstname"] + " " + self.credentials["lastname"]
            self.assertEqual(username_element.text, expected_username)
        except Exception as e:
            self.fail(f"Username not found or empty: {e}")

if __name__ == "__main__":
    unittest.main()