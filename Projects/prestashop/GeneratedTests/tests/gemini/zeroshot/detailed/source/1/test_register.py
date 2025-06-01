import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign in')]")
        sign_in_link = self.wait.until(EC.presence_of_element_located(sign_in_link_locator))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
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
        gender_radio_locator = (By.ID, "field-id_gender-1")
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
        #newsletter_checkbox.click() # Not required

        customer_privacy_checkbox_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = self.wait.until(EC.presence_of_element_located(customer_privacy_checkbox_locator))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        submit_button = self.wait.until(EC.presence_of_element_located(submit_button_locator))
        submit_button.click()

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful.
        sign_out_locator = (By.LINK_TEXT, "Sign out")
        try:
            sign_out_element = self.wait.until(EC.presence_of_element_located(sign_out_locator))
            sign_out_text = sign_out_element.text
        except:
            self.fail("Sign out link not found after registration")

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//span[contains(.,'Test User')]")
        try:
            username_element = self.wait.until(EC.presence_of_element_located(username_locator))
            username_text = username_element.text
        except:
            self.fail("Username not found after registration")

        if not sign_out_text:
            self.fail("Sign out text is empty")

        if "Sign out" not in sign_out_text:
            self.fail(f"Sign out text not found. Actual text: {sign_out_text}")
        
        if not username_text:
            self.fail("Username text is empty")

        if "Test User" not in username_text:
            self.fail(f"Username text not found. Actual text: {username_text}")

if __name__ == "__main__":
    unittest.main()