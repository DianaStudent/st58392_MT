import unittest
import uuid
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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage.
        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = self.wait.until(EC.presence_of_element_located(sign_in_link_locator))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]")
        register_link = self.wait.until(EC.presence_of_element_located(register_link_locator))
        register_link.click()

        # 4. Fill in the registration form.
        gender = "1"
        firstname = "Test"
        lastname = "User"
        email = f"test_{uuid.uuid4().hex}@user.com"
        password = "test@user1"
        birthday = "01/01/2000"

        # Select gender
        gender_radio_locator = (By.ID, f"field-id_gender-{gender}")
        gender_radio = self.wait.until(EC.presence_of_element_located(gender_radio_locator))
        gender_radio.click()

        # Fill in first name
        firstname_field_locator = (By.ID, "field-firstname")
        firstname_field = self.wait.until(EC.presence_of_element_located(firstname_field_locator))
        firstname_field.send_keys(firstname)

        # Fill in last name
        lastname_field_locator = (By.ID, "field-lastname")
        lastname_field = self.wait.until(EC.presence_of_element_located(lastname_field_locator))
        lastname_field.send_keys(lastname)

        # Fill in email
        email_field_locator = (By.ID, "field-email")
        email_field = self.wait.until(EC.presence_of_element_located(email_field_locator))
        email_field.send_keys(email)

        # Fill in password
        password_field_locator = (By.ID, "field-password")
        password_field = self.wait.until(EC.presence_of_element_located(password_field_locator))
        password_field.send_keys(password)

        # Fill in birthday
        birthday_field_locator = (By.ID, "field-birthday")
        birthday_field = self.wait.until(EC.presence_of_element_located(birthday_field_locator))
        birthday_field.send_keys(birthday)

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_checkbox_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = self.wait.until(EC.presence_of_element_located(psgdpr_checkbox_locator))
        psgdpr_checkbox.click()

        newsletter_checkbox_locator = (By.NAME, "newsletter")
        newsletter_checkbox = self.wait.until(EC.presence_of_element_located(newsletter_checkbox_locator))
        # newsletter_checkbox.click()  # Optional, not required

        customer_privacy_checkbox_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = self.wait.until(EC.presence_of_element_located(customer_privacy_checkbox_locator))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        submit_button = self.wait.until(EC.presence_of_element_located(submit_button_locator))
        submit_button.click()

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful by checking that:
        #    - The "Sign out" button is present in the top navigation
        #    - The username (e.g. "test user") is also visible in the top navigation.

        sign_out_button_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        try:
            sign_out_button = self.wait.until(EC.presence_of_element_located(sign_out_button_locator))
            sign_out_text = sign_out_button.text
            self.assertIn("Sign out", sign_out_text)
        except:
            self.fail("Sign out button not found after registration.")

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")
        try:
            username_element = self.wait.until(EC.presence_of_element_located(username_locator))
            username_text = username_element.text
            self.assertEqual("Test User", username_text)
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()