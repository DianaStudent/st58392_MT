from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
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
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        try:
            sign_in_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(text(),'Sign in')]")))
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        try:
            register_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='no-account']/a[contains(text(),'Create one here')]")))
            register_link.click()
        except Exception as e:
            self.fail(f"Could not find or click register link: {e}")

        # 4. Fill in the registration form.
        try:
            # Generate dynamic email
            email = "test_" + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + "@user.com"

            # Select Gender (Mr.)
            mr_radio = self.wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
            mr_radio.click()

            # Fill First Name
            firstname_input = self.wait.until(EC.element_to_be_clickable((By.ID, "field-firstname")))
            firstname_input.send_keys("Test")

            # Fill Last Name
            lastname_input = self.wait.until(EC.element_to_be_clickable((By.ID, "field-lastname")))
            lastname_input.send_keys("User")

            # Fill Email
            email_input = self.wait.until(EC.element_to_be_clickable((By.ID, "field-email")))
            email_input.send_keys(email)

            # Fill Password
            password_input = self.wait.until(EC.element_to_be_clickable((By.ID, "field-password")))
            password_input.send_keys("test@user1")

            # Fill Birthday
            birthday_input = self.wait.until(EC.element_to_be_clickable((By.ID, "field-birthday")))
            birthday_input.send_keys("01/01/2000")

        except Exception as e:
            self.fail(f"Could not fill registration form: {e}")

        # 5. Tick checkboxes.
        try:
            # Tick "I agree to the terms and conditions and the privacy policy"
            psgdpr_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "psgdpr")))
            psgdpr_checkbox.click()

            #Tick "Customer data privacy"
            customer_privacy_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer_privacy")))
            customer_privacy_checkbox.click()

            #Tick "Sign up for our newsletter"
            newsletter_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "newsletter")))
            newsletter_checkbox.click()

        except Exception as e:
            self.fail(f"Could not tick checkboxes: {e}")

        # 6. Submit the registration form.
        try:
            save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary form-control-submit float-xs-right']")))
            save_button.click()
        except Exception as e:
            self.fail(f"Could not submit registration form: {e}")

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful.
        try:
            # Check for "Sign out" link
            sign_out_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign out')]")))
            self.assertIsNotNone(sign_out_link, "Sign out link not found after registration.")

            # Check for username
            username_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='account']/span")))
            self.assertIsNotNone(username_element, "Username element not found after registration.")
            username_text = username_element.text
            self.assertEqual(username_text, "Test User", "Incorrect username after registration.")

        except Exception as e:
            self.fail(f"Registration confirmation failed: {e}")

if __name__ == "__main__":
    unittest.main()