import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]"))
        )
        if register_link:
            register_link.click()
        else:
            self.fail("Registration link not found")

        # 4. Fill in the following fields using credentials:
        #    - Gender, First name, Last name, Email, Password, Birthday
        gender = "1"
        firstname = "Test"
        lastname = "User"
        email = "test_" + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + "@user.com"
        password = "test@user1"
        birthday = "01/01/2000"

        # Gender
        gender_radio_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-id_gender-" + gender))
        )
        if gender_radio_button:
            gender_radio_button.click()
        else:
            self.fail("Gender radio button not found")

        # First name
        firstname_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        if firstname_input:
            firstname_input.send_keys(firstname)
        else:
            self.fail("First name input not found")

        # Last name
        lastname_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        if lastname_input:
            lastname_input.send_keys(lastname)
        else:
            self.fail("Last name input not found")

        # Email
        email_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        if email_input:
            email_input.send_keys(email)
        else:
            self.fail("Email input not found")

        # Password
        password_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        if password_input:
            password_input.send_keys(password)
        else:
            self.fail("Password input not found")

        # Birthday
        birthday_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        if birthday_input:
            birthday_input.send_keys(birthday)
        else:
            self.fail("Birthday input not found")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_checkbox = self.wait.until(
            EC.presence_of_element_located((By.NAME, "psgdpr"))
        )
        if psgdpr_checkbox:
            psgdpr_checkbox.click()
        else:
            self.fail("psgdpr checkbox not found")

        customer_privacy_checkbox = self.wait.until(
            EC.presence_of_element_located((By.NAME, "customer_privacy"))
        )
        if customer_privacy_checkbox:
            customer_privacy_checkbox.click()
        else:
            self.fail("customer_privacy checkbox not found")

        # 6. Submit the registration form.
        save_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//footer[@class='form-footer clearfix']/button[@type='submit']"))
        )
        if save_button:
            save_button.click()
        else:
            self.fail("Save button not found")

        # 7. Wait for the redirect after login.
        # 8. Confirm that login was successful by checking that:
        #    - The "Sign out" button is present in the top navigation
        #    - The username (e.g. "test user") is also visible in the top navigation.

        sign_out_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'logout')]"))
        )

        if not sign_out_link:
            self.fail("Sign out link not found after registration")

        sign_out_text = sign_out_link.text
        if not sign_out_text or "Sign out" not in sign_out_text:
            self.fail(f"Sign out text is incorrect: {sign_out_text}")

        username_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]"))
        )

        if not username_link:
            self.fail("Username link not found after registration")

        username_text = username_link.text
        expected_username = firstname + " " + lastname
        if not username_text or expected_username not in username_text:
            self.fail(f"Username text is incorrect: {username_text}, expected {expected_username}")


if __name__ == "__main__":
    unittest.main()