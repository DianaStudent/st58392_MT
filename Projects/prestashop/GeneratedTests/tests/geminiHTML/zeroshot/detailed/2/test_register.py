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
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]")))
        register_link.click()

        # 4. Fill in the registration form.
        # Generate dynamic email
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"

        # Gender
        mr_radio = self.wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        mr_radio.click()

        # First name
        firstname_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        firstname_field.send_keys("Test")

        # Last name
        lastname_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        lastname_field.send_keys("User")

        # Email
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_field.send_keys(email)

        # Password
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_field.send_keys("test@user1")

        # Birthday
        birthday_field = self.wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday_field.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # I agree to the terms and conditions and the privacy policy
        psgdpr_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        psgdpr_checkbox.click()

        # Customer data privacy
        customer_privacy_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'form-control-submit')]")))
        save_button.click()

        # 7. Wait for the redirect after login.
        self.wait.until(EC.url_contains("my-account"))

        # 8. Confirm that login was successful.
        # - The "Sign out" button is present in the top navigation
        sign_out_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")))
        sign_out_text = sign_out_link.text
        if not sign_out_text:
            self.fail("Sign out link text is empty")
        self.assertEqual(sign_out_text.strip(), "Sign out", "Sign out link not found")

        # - The username (e.g. "Test User") is also visible in the top navigation.
        username_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")))
        username_text = username_link.text
        if not username_text:
            self.fail("Username link text is empty")
        self.assertEqual(username_text.strip(), "Test User", "Username not found")


if __name__ == "__main__":
    unittest.main()