import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign in')]"))
        )
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(.,'Create one here')]"))
        )
        register_link.click()

        # 4. Fill in the following fields using credentials:
        #    - Gender, First name, Last name, Email, Password, Birthday
        gender = "1"
        firstname = "Test"
        lastname = "User"
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test@user1"
        birthday = "01/01/2000"

        # Gender
        gender_radio_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-id_gender-{}".format(gender)))
        )
        gender_radio_button.click()

        # First name
        firstname_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        firstname_field.send_keys(firstname)

        # Last name
        lastname_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        lastname_field.send_keys(lastname)

        # Email
        email_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        email_field.send_keys(email)

        # Password
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        password_field.send_keys(password)

        # Birthday
        birthday_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        birthday_field.send_keys(birthday)

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # I agree to the terms and conditions and the privacy policy
        psgdpr_checkbox = self.wait.until(
            EC.presence_of_element_located((By.NAME, "psgdpr"))
        )
        psgdpr_checkbox.click()

        # Customer data privacy
        customer_privacy_checkbox = self.wait.until(
            EC.presence_of_element_located((By.NAME, "customer_privacy"))
        )
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(.,'Save')]"))
        )
        save_button.click()

        # 7. Wait for the redirect after login.

        # 8. Confirm that login was successful by checking that:
        #    - The "Sign out" button is present in the top navigation
        #    - The username (e.g. "test user") is also visible in the top navigation.
        try:
            sign_out_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign out')]"))
            )
            self.assertTrue("Sign out" in sign_out_link.text)

            username_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[@class='account']/span"))
            )

            if username_element and username_element.text:
                expected_username = f"{firstname} {lastname}"
                self.assertEqual(username_element.text, expected_username, "Username mismatch")
            else:
                self.fail("Username element not found or empty.")

        except Exception as e:
            self.fail(f"Login verification failed: {e}")


if __name__ == "__main__":
    unittest.main()