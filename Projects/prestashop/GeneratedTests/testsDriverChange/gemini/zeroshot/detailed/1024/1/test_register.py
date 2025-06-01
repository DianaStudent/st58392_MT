import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage (done in setUp)

        # 2. Click the login link from the top navigation
        try:
            sign_in_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'login')]")))
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        try:
            register_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'registration')]")))
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click register link: {e}")

        # 4. Fill in the registration form
        email = f"test_{random.randint(100000, 999999)}@user.com"

        try:
            # Gender
            mr_radio = self.wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
            mr_radio.click()

            # First name
            firstname_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
            firstname_input.send_keys("Test")

            # Last name
            lastname_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
            lastname_input.send_keys("User")

            # Email
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
            email_input.send_keys(email)

            # Password
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))
            password_input.send_keys("test@user1")

            # Birthday
            birthday_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
            birthday_input.send_keys("01/01/2000")

        except Exception as e:
            self.fail(f"Could not fill in form fields: {e}")

        # 5. Tick checkboxes
        try:
            # Agree to terms and conditions
            psgdpr_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
            psgdpr_checkbox.click()

            # Customer Privacy
            customer_privacy_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
            customer_privacy_checkbox.click()

            #Newsletter
            newsletter_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "newsletter")))
            newsletter_checkbox.click()

        except Exception as e:
            self.fail(f"Could not tick checkboxes: {e}")

        # 6. Submit the registration form
        try:
            save_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(text(), 'Save')]")))
            save_button.click()
        except Exception as e:
            self.fail(f"Could not submit the form: {e}")

        # 7. Wait for redirect after login
        time.sleep(2)

        # 8. Confirm successful login
        try:
            # Check for "Sign out" link
            sign_out_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed")

            # Check for username
            username_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'my-account')]/span[not(contains(@class, 'hidden-sm-down'))]")))
            username = username_element.text
            self.assertEqual(username, "Test User", "Username is not correct")

        except Exception as e:
            self.fail(f"Login confirmation failed: {e}")

if __name__ == "__main__":
    unittest.main()