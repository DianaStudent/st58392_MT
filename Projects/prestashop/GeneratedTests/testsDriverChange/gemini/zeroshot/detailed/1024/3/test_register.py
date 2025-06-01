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
        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(text(),'Sign in')]")
        sign_in_link = self.wait.until(EC.presence_of_element_located(sign_in_link_locator))
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = self.wait.until(EC.presence_of_element_located(register_link_locator))
        register_link.click()

        # 4. Fill in the following fields using credentials:
        #    - Gender, First name, Last name, Email, Password, Birthday
        gender_mr_locator = (By.ID, "field-id_gender-1")
        gender_mr = self.wait.until(EC.presence_of_element_located(gender_mr_locator))
        gender_mr.click()

        firstname_locator = (By.ID, "field-firstname")
        firstname_input = self.wait.until(EC.presence_of_element_located(firstname_locator))
        firstname_input.send_keys("Test")

        lastname_locator = (By.ID, "field-lastname")
        lastname_input = self.wait.until(EC.presence_of_element_located(lastname_locator))
        lastname_input.send_keys("User")

        email_locator = (By.ID, "field-email")
        email_input = self.wait.until(EC.presence_of_element_located(email_locator))
        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"
        email_input.send_keys(email)

        password_locator = (By.ID, "field-password")
        password_input = self.wait.until(EC.presence_of_element_located(password_locator))
        password_input.send_keys("test@user1")

        birthday_locator = (By.ID, "field-birthday")
        birthday_input = self.wait.until(EC.presence_of_element_located(birthday_locator))
        birthday_input.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = self.wait.until(EC.presence_of_element_located(psgdpr_locator))
        psgdpr_checkbox.click()

        newsletter_locator = (By.NAME, "newsletter")
        newsletter_checkbox = self.wait.until(EC.presence_of_element_located(newsletter_locator))
        newsletter_checkbox.click()

        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = self.wait.until(EC.presence_of_element_located(customer_privacy_locator))
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        save_button = self.wait.until(EC.presence_of_element_located(save_button_locator))
        save_button.click()

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful by checking that:
        #    - The "Sign out" button is present in the top navigation
        #    - The username (e.g. "test user") is also visible in the top navigation.
        sign_out_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(text(),'Sign out')]")
        try:
            sign_out_button = self.wait.until(EC.presence_of_element_located(sign_out_locator))
            self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not displayed")
        except:
            self.fail("Sign out button not found after registration.")

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[@class='account']/span")
        try:
            username_element = self.wait.until(EC.presence_of_element_located(username_locator))
            username = username_element.text
            self.assertEqual(username, "Test User", "Username is not correct")
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()