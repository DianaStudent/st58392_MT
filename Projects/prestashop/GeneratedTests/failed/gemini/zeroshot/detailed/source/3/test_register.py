from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign in')]")
        sign_in_link = self.wait.until(EC.element_to_be_clickable(sign_in_link_locator))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = self.wait.until(EC.element_to_be_clickable(register_link_locator))
        register_link.click()

        # 4. Fill in the registration form.
        # Generate dynamic email
        email = f"test_{uuid.uuid4().hex[:6]}@user.com"

        # Gender
        mr_radio_locator = (By.ID, "field-id_gender-1")
        mr_radio = self.wait.until(EC.presence_of_element_located(mr_radio_locator))
        mr_radio.click()

        # First name
        firstname_locator = (By.ID, "field-firstname")
        firstname_input = self.wait.until(EC.element_to_be_clickable(firstname_locator))
        firstname_input.send_keys("Test")

        # Last name
        lastname_locator = (By.ID, "field-lastname")
        lastname_input = self.wait.until(EC.element_to_be_clickable(lastname_locator))
        lastname_input.send_keys("User")

        # Email
        email_locator = (By.ID, "field-email")
        email_input = self.wait.until(EC.element_to_be_clickable(email_locator))
        email_input.send_keys(email)

        # Password
        password_locator = (By.ID, "field-password")
        password_input = self.wait.until(EC.element_to_be_clickable(password_locator))
        password_input.send_keys("test@user1")

        # Birthday
        birthday_locator = (By.ID, "field-birthday")
        birthday_input = self.wait.until(EC.element_to_be_clickable(birthday_locator))
        birthday_input.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # I agree to the terms and conditions and the privacy policy
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = self.wait.until(EC.element_to_be_clickable(psgdpr_locator))
        psgdpr_checkbox.click()

        # Customer data privacy
        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = self.wait.until(EC.element_to_be_clickable(customer_privacy_locator))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        save_button = self.wait.until(EC.element_to_be_clickable(save_button_locator))
        save_button.click()

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful by checking that:
        #    - The "Sign out" button is present in the top navigation
        #    - The username (e.g. "test user") is also visible in the top navigation.
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign out')]")
        try:
            self.wait.until(EC.element_to_be_clickable(sign_out_link_locator))
        except:
            self.fail("Sign out link not found after registration.")

        sign_out_link = self.driver.find_element(*sign_out_link_locator)
        if not sign_out_link.text:
            self.fail("Sign out link text is empty.")
        self.assertEqual("Sign out", sign_out_link.text)

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[@class='account']/span")
        try:
            self.wait.until(EC.presence_of_element_located(username_locator))
        except:
            self.fail("Username not found after registration.")

        username_element = self.driver.find_element(*username_locator)
        if not username_element.text:
            self.fail("Username text is empty.")
        self.assertEqual("Test User", username_element.text)

if __name__ == "__main__":
    unittest.main()