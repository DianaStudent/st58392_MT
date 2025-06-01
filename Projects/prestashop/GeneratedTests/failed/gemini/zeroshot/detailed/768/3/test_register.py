from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = wait.until(EC.element_to_be_clickable(sign_in_link_locator))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]")
        register_link = wait.until(EC.element_to_be_clickable(register_link_locator))
        register_link.click()

        # 4. Fill in the registration form.
        # Gender
        gender_locator = (By.ID, "field-id_gender-1")
        gender_radio = wait.until(EC.presence_of_element_located(gender_locator))
        gender_radio.click()

        # First name
        firstname_locator = (By.ID, "field-firstname")
        firstname_input = wait.until(EC.element_to_be_clickable(firstname_locator))
        firstname_input.send_keys(self.credentials['firstname'])

        # Last name
        lastname_locator = (By.ID, "field-lastname")
        lastname_input = wait.until(EC.element_to_be_clickable(lastname_locator))
        lastname_input.send_keys(self.credentials['lastname'])

        # Email
        email_locator = (By.ID, "field-email")
        email_input = wait.until(EC.element_to_be_clickable(email_locator))
        email_input.send_keys(self.credentials['email'])

        # Password
        password_locator = (By.ID, "field-password")
        password_input = wait.until(EC.element_to_be_clickable(password_locator))
        password_input.send_keys(self.credentials['password'])

        # Birthday
        birthday_locator = (By.ID, "field-birthday")
        birthday_input = wait.until(EC.element_to_be_clickable(birthday_locator))
        birthday_input.send_keys(self.credentials['birthday'])

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = wait.until(EC.element_to_be_clickable(psgdpr_locator))
        psgdpr_checkbox.click()

        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = wait.until(EC.element_to_be_clickable(customer_privacy_locator))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        submit_button = wait.until(EC.element_to_be_clickable(submit_button_locator))
        submit_button.click()

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful
        sign_out_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        try:
            sign_out_button = wait.until(EC.element_to_be_clickable(sign_out_locator))
            self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not displayed")
        except:
            self.fail("Sign out button not found after registration.")

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']")
        try:
            username_element = wait.until(EC.presence_of_element_located(username_locator))
            username_text = username_element.text
            self.assertIn(self.credentials['firstname'], username_text, "Username is not displayed correctly")
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()