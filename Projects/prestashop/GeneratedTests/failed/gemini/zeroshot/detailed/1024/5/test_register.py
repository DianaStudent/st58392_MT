from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
import random
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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = self.wait.until(EC.element_to_be_clickable(sign_in_link_locator))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.XPATH, "//div[@class='no-account']//a[contains(@href, 'registration')]")
        register_link = self.wait.until(EC.element_to_be_clickable(register_link_locator))
        register_link.click()

        # 4. Fill in the registration form.
        # Gender
        gender_locator = (By.ID, "field-id_gender-1")
        gender_radio = self.wait.until(EC.presence_of_element_located(gender_locator))
        gender_radio.click()

        # First name
        firstname_locator = (By.ID, "field-firstname")
        firstname_input = self.wait.until(EC.element_to_be_clickable(firstname_locator))
        firstname_input.send_keys("Test")

        # Last name
        lastname_locator = (By.ID, "field-lastname")
        lastname_input = self.wait.until(EC.element_to_be_clickable(lastname_locator))
        lastname_input.send_keys("User")

        # Email
        email = f"test_{random.randint(100000, 999999)}@user.com"
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
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = self.wait.until(EC.element_to_be_clickable(psgdpr_locator))
        psgdpr_checkbox.click()

        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = self.wait.until(EC.element_to_be_clickable(customer_privacy_locator))
        customer_privacy_checkbox.click()

        # Newsletter
        newsletter_locator = (By.NAME, "newsletter")
        newsletter_checkbox = self.wait.until(EC.element_to_be_clickable(newsletter_locator))
        newsletter_checkbox.click()

        # 6. Submit the registration form.
        save_button_locator = (By.XPATH, "//footer[@class='form-footer clearfix']//button[@type='submit']")
        save_button = self.wait.until(EC.element_to_be_clickable(save_button_locator))
        save_button.click()

        # 7. Wait for the redirect after login.
        # Assuming redirect to homepage after successful registration

        # 8. Confirm that login was successful.
        # Check for "Sign out" button
        sign_out_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        try:
            sign_out_button = self.wait.until(EC.element_to_be_clickable(sign_out_locator))
            sign_out_text = sign_out_button.text
            self.assertEqual(sign_out_text.strip(), "Sign out", "Sign out button not found.")
        except:
            self.fail("Sign out button not found after registration.")

        # Check for username
        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//span[contains(text(), 'Test User')]")
        try:
            username_element = self.wait.until(EC.presence_of_element_located(username_locator))
            username_text = username_element.text
            self.assertEqual(username_text.strip(), "Test User", "Username not found.")
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()