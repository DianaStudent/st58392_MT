import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
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
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = wait.until(EC.presence_of_element_located(register_link_locator))
        register_link.click()

        # 4. Fill in the registration form.
        # Generate dynamic email
        random_num = random.randint(100000, 999999)
        email = f"test_{random_num}@user.com"

        # Select Gender (Mr.)
        mr_radio_locator = (By.ID, "field-id_gender-1")
        mr_radio = wait.until(EC.presence_of_element_located(mr_radio_locator))
        mr_radio.click()

        # First name
        firstname_locator = (By.ID, "field-firstname")
        firstname_input = wait.until(EC.presence_of_element_located(firstname_locator))
        firstname_input.send_keys("Test")

        # Last name
        lastname_locator = (By.ID, "field-lastname")
        lastname_input = wait.until(EC.presence_of_element_located(lastname_locator))
        lastname_input.send_keys("User")

        # Email
        email_locator = (By.ID, "field-email")
        email_input = wait.until(EC.presence_of_element_located(email_locator))
        email_input.send_keys(email)

        # Password
        password_locator = (By.ID, "field-password")
        password_input = wait.until(EC.presence_of_element_located(password_locator))
        password_input.send_keys("test@user1")

        # Birthday
        birthday_locator = (By.ID, "field-birthday")
        birthday_input = wait.until(EC.presence_of_element_located(birthday_locator))
        birthday_input.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # psgdpr (Terms and conditions and the privacy policy)
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = wait.until(EC.presence_of_element_located(psgdpr_locator))
        psgdpr_checkbox.click()

        # customer_privacy (Customer data privacy)
        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = wait.until(EC.presence_of_element_located(customer_privacy_locator))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        save_button = wait.until(EC.presence_of_element_located(save_button_locator))
        save_button.click()

        # 7. Wait for the redirect after login.
        # Assuming redirect to homepage after registration
        wait.until(EC.url_to_be("http://localhost:8080/en/"))

        # 8. Confirm that login was successful
        # Check for "Sign out" link
        sign_out_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")
        try:
            sign_out_link = wait.until(EC.presence_of_element_located(sign_out_link_locator))
            sign_out_text = sign_out_link.text
            self.assertEqual(sign_out_text, "Sign out", "Sign out link not found after registration.")
        except:
            self.fail("Sign out link not found after registration.")

        # Check for username
        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span")
        try:
            username_element = wait.until(EC.presence_of_element_located(username_locator))
            username_text = username_element.text
            self.assertEqual(username_text, "Test User", "Username not found after registration.")
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()