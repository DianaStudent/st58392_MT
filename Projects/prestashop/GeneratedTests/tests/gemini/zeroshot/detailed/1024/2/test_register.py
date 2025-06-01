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
        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")))
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        create_account_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]")))
        if create_account_link:
            create_account_link.click()
        else:
            self.fail("Create account link not found")

        # 4. Fill in the registration form.
        gender_mr_radio = self.wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        if gender_mr_radio:
            gender_mr_radio.click()
        else:
            self.fail("Gender Mr. radio button not found")

        firstname_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        lastname_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        birthday_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        
        if not all([firstname_input, lastname_input, email_input, password_input, birthday_input]):
            self.fail("One or more input fields not found")

        firstname_input.send_keys("Test")
        lastname_input.send_keys("User")
        email = f"test_{random.randint(100000, 999999)}@user.com"
        email_input.send_keys(email)
        password_input.send_keys("test@user1")
        birthday_input.send_keys("01/01/2000")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        newsletter_checkbox = self.driver.find_element(By.NAME, "newsletter")
        customer_privacy_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))

        if not all([psgdpr_checkbox, customer_privacy_checkbox]):
            self.fail("One or more checkboxes not found")

        psgdpr_checkbox.click()
        if newsletter_checkbox:
            newsletter_checkbox.click()
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'form-control-submit')]")))
        if save_button:
            save_button.click()
        else:
            self.fail("Save button not found")

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful.
        sign_out_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]")))
        username_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//span[contains(text(), 'Test User')]")))

        if not sign_out_link:
            self.fail("Sign out link not found after registration")
        if not username_element:
            self.fail("Username element not found after registration")

        sign_out_text = sign_out_link.text if sign_out_link.text else ""
        username_text = username_element.text if username_element.text else ""

        if "Sign out" not in sign_out_text:
            self.fail(f"Sign out link text is incorrect: {sign_out_text}")
        if "Test User" not in username_text:
            self.fail(f"Username is incorrect: {username_text}")

if __name__ == "__main__":
    unittest.main()