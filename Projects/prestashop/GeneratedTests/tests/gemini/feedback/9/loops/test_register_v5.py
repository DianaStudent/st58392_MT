import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        sign_in_link = wait.until(EC.presence_of_element_located(sign_in_link_locator))
        self.assertTrue(sign_in_link.is_displayed(), "Sign-in link is not displayed.")
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = wait.until(EC.presence_of_element_located(register_link_locator))
        self.assertTrue(register_link.is_displayed(), "Register link is not displayed.")
        register_link.click()

        # 4. Fill in the registration form.
        # Generate dynamic email
        random_num = random.randint(100000, 999999)
        email = f"test_{random_num}@user.com"

        # Select Gender (Mr.)
        mr_radio_locator = (By.ID, "field-id_gender-1")
        mr_radio = wait.until(EC.presence_of_element_located(mr_radio_locator))
        self.assertTrue(mr_radio.is_displayed(), "Mr. radio button is not displayed.")
        mr_radio.click()

        # First name
        firstname_locator = (By.ID, "field-firstname")
        firstname_input = wait.until(EC.presence_of_element_located(firstname_locator))
        self.assertTrue(firstname_input.is_displayed(), "First name input is not displayed.")
        firstname_input.send_keys("Test")

        # Last name
        lastname_locator = (By.ID, "field-lastname")
        lastname_input = wait.until(EC.presence_of_element_located(lastname_locator))
        self.assertTrue(lastname_input.is_displayed(), "Last name input is not displayed.")
        lastname_input.send_keys("User")

        # Email
        email_locator = (By.ID, "field-email")
        email_input = wait.until(EC.presence_of_element_located(email_locator))
        self.assertTrue(email_input.is_displayed(), "Email input is not displayed.")
        email_input.send_keys(email)

        # Password
        password_locator = (By.ID, "field-password")
        password_input = wait.until(EC.presence_of_element_located(password_locator))
        self.assertTrue(password_input.is_displayed(), "Password input is not displayed.")
        password_input.send_keys("test@user1")

        # Birthday
        birthday_locator = (By.ID, "field-birthday")
        birthday_input = wait.until(EC.presence_of_element_located(birthday_locator))
        self.assertTrue(birthday_input.is_displayed(), "Birthday input is not displayed.")
        birthday_input.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # psgdpr (Terms and conditions and the privacy policy)
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = wait.until(EC.element_to_be_clickable(psgdpr_locator))
        self.assertTrue(psgdpr_checkbox.is_displayed(), "psgdpr checkbox is not displayed.")
        psgdpr_checkbox.click()

        # customer_privacy (Customer data privacy)
        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = wait.until(EC.element_to_be_clickable(customer_privacy_locator))
        self.assertTrue(customer_privacy_checkbox.is_displayed(), "customer_privacy checkbox is not displayed.")
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        save_button = wait.until(EC.element_to_be_clickable(save_button_locator))
        self.assertTrue(save_button.is_displayed(), "Save button is not displayed.")
        save_button.click()

        # 7. Wait for the redirect after login.
        # Assuming redirect to homepage after registration
        wait.until(EC.url_to_be("http://localhost:8080/en/"))

        # 8. Confirm that login was successful
        # Check for "Sign out" link
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        try:
            sign_out_link = wait.until(EC.presence_of_element_located(sign_out_link_locator))
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed.")
            sign_out_text = sign_out_link.text
            self.assertEqual(sign_out_text, "Sign out", "Sign out link not found after registration.")
        except:
            self.fail("Sign out link not found after registration.")

        # Check for username
        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span")
        try:
            username_element = wait.until(EC.presence_of_element_located(username_locator))
            self.assertTrue(username_element.is_displayed(), "Username element is not displayed.")
            username_text = username_element.text
            self.assertEqual(username_text, "Test User", "Username not found after registration.")
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()