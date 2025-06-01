import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage. (Done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']/div/a[contains(@href, 'login')]")
        sign_in_link = wait.until(EC.presence_of_element_located(sign_in_link_locator))
        self.assertIsNotNone(sign_in_link, "Sign-in link not found.")
        self.assertTrue(sign_in_link.is_displayed(), "Sign-in link is not displayed.")
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = wait.until(EC.presence_of_element_located(register_link_locator))
        self.assertIsNotNone(register_link, "Register link not found.")
        self.assertTrue(register_link.is_displayed(), "Register link is not displayed.")
        register_link.click()

        # 4. Fill in the registration form.
        gender = "1"
        firstname = "Test"
        lastname = "User"
        email = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"
        password = "test@user1"
        birthday = "01/01/2000"

        # Select gender
        gender_radio_locator = (By.ID, "field-id_gender-" + gender)
        gender_radio = wait.until(EC.presence_of_element_located(gender_radio_locator))
        self.assertIsNotNone(gender_radio, "Gender radio button not found.")
        self.assertTrue(gender_radio.is_displayed(), "Gender radio button is not displayed.")
        gender_radio.click()

        # Fill in first name
        firstname_field_locator = (By.ID, "field-firstname")
        firstname_field = wait.until(EC.presence_of_element_located(firstname_field_locator))
        self.assertIsNotNone(firstname_field, "First name field not found.")
        self.assertTrue(firstname_field.is_displayed(), "First name field is not displayed.")
        firstname_field.send_keys(firstname)

        # Fill in last name
        lastname_field_locator = (By.ID, "field-lastname")
        lastname_field = wait.until(EC.presence_of_element_located(lastname_field_locator))
        self.assertIsNotNone(lastname_field, "Last name field not found.")
        self.assertTrue(lastname_field.is_displayed(), "Last name field is not displayed.")
        lastname_field.send_keys(lastname)

        # Fill in email
        email_field_locator = (By.ID, "field-email")
        email_field = wait.until(EC.presence_of_element_located(email_field_locator))
        self.assertIsNotNone(email_field, "Email field not found.")
        self.assertTrue(email_field.is_displayed(), "Email field is not displayed.")
        email_field.send_keys(email)

        # Fill in password
        password_field_locator = (By.ID, "field-password")
        password_field = wait.until(EC.presence_of_element_located(password_field_locator))
        self.assertIsNotNone(password_field, "Password field not found.")
        self.assertTrue(password_field.is_displayed(), "Password field is not displayed.")
        password_field.send_keys(password)

        # Fill in birthday
        birthday_field_locator = (By.ID, "field-birthday")
        birthday_field = wait.until(EC.presence_of_element_located(birthday_field_locator))
        self.assertIsNotNone(birthday_field, "Birthday field not found.")
        self.assertTrue(birthday_field.is_displayed(), "Birthday field is not displayed.")
        birthday_field.send_keys(birthday)

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_checkbox_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = wait.until(EC.presence_of_element_located(psgdpr_checkbox_locator))
        self.assertIsNotNone(psgdpr_checkbox, "psgdpr checkbox not found.")
        self.assertTrue(psgdpr_checkbox.is_displayed(), "psgdpr checkbox is not displayed.")
        psgdpr_checkbox.click()

        customer_privacy_checkbox_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = wait.until(EC.presence_of_element_located(customer_privacy_checkbox_locator))
        self.assertIsNotNone(customer_privacy_checkbox, "customer_privacy checkbox not found.")
        self.assertTrue(customer_privacy_checkbox.is_displayed(), "customer_privacy checkbox is not displayed.")
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button_locator = (By.XPATH, "//footer[@class='form-footer clearfix']/button[@type='submit']")
        save_button = wait.until(EC.presence_of_element_located(save_button_locator))
        self.assertIsNotNone(save_button, "Save button not found.")
        self.assertTrue(save_button.is_displayed(), "Save button is not displayed.")
        save_button.click()

        # 7. Wait for the redirect after login.

        # 8. Confirm that login was successful.
        # Check for "Sign out" link
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        try:
            sign_out_link = wait.until(EC.presence_of_element_located(sign_out_link_locator))
            self.assertIsNotNone(sign_out_link, "Sign out link not found after registration.")
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed.")
            sign_out_text = sign_out_link.text
            self.assertEqual(sign_out_text, "Sign out", "Sign out link text incorrect.")
        except:
            self.fail("Sign out link not found after registration.")

        # Check for username
        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]/span")
        try:
            username_element = wait.until(EC.presence_of_element_located(username_locator))
            self.assertIsNotNone(username_element, "Username element not found after registration.")
            self.assertTrue(username_element.is_displayed(), "Username element is not displayed.")
            username_text = username_element.text
            expected_username = firstname + " " + lastname
            self.assertEqual(username_text, expected_username, "Username not found or incorrect after registration.")
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()