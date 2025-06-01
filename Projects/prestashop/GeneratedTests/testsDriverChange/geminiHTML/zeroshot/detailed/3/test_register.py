import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email = 'test_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + '@user.com'
        self.credentials = {
            'gender': '1',
            'firstname': 'Test',
            'lastname': 'User',
            'email': self.email,
            'password': 'test@user1',
            'birthday': '01/01/2000'
        }

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage.
        # 2. Click the login link from the top navigation.
        try:
            sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")))
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click register link: {e}")

        # 4. Fill in the registration form.
        try:
            # Gender
            gender_radio_button = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
            gender_radio_button.click()

            # First name
            firstname_input = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
            firstname_input.send_keys(self.credentials['firstname'])

            # Last name
            lastname_input = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
            lastname_input.send_keys(self.credentials['lastname'])

            # Email
            email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
            email_input.send_keys(self.credentials['email'])

            # Password
            password_input = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
            password_input.send_keys(self.credentials['password'])

            # Birthday
            birthday_input = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
            birthday_input.send_keys(self.credentials['birthday'])

        except Exception as e:
            self.fail(f"Could not fill in registration form: {e}")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        try:
            # Privacy checkbox
            privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
            privacy_checkbox.click()

            # Terms and conditions checkbox
            terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
            terms_checkbox.click()

            # Newsletter checkbox
            newsletter_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "newsletter")))
            newsletter_checkbox.click()

        except Exception as e:
            self.fail(f"Could not tick checkboxes: {e}")

        # 6. Submit the registration form.
        try:
            save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'form-control-submit')]")))
            save_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful.
        try:
            # Check for "Sign out" link
            sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            self.assertIsNotNone(sign_out_link, "Sign out link not found after registration.")

            # Check for username
            account_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'my-account')]//span")))
            username = account_link.text
            self.assertIn("Test User", username, "Username not found after registration.")

        except Exception as e:
            self.fail(f"Registration confirmation failed: {e}")

if __name__ == "__main__":
    unittest.main()