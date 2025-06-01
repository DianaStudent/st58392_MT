import unittest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email = f"test_{uuid.uuid4().hex[:6]}@user.com"
        self.firstname = "Test"
        self.lastname = "User"
        self.password = "test@user1"
        self.birthday = "01/01/2000"
        self.gender = "1"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Open the homepage (already done in setUp)

        # 2. Click the login link from the top navigation.
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
        )
        sign_in_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='no-account']/a[contains(@href, 'registration')]"))
        )
        register_link.click()

        # 4. Fill in the registration form.
        # Gender
        gender_radio_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-id_gender-1"))
        )
        gender_radio_button.click()

        # First name
        firstname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        firstname_input.send_keys(self.firstname)

        # Last name
        lastname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        lastname_input.send_keys(self.lastname)

        # Email
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        email_input.send_keys(self.email)

        # Password
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        password_input.send_keys(self.password)

        # Birthday
        birthday_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        birthday_input.send_keys(self.birthday)

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # psgdpr
        psgdpr_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "psgdpr"))
        )
        psgdpr_checkbox.click()

        # customer_privacy
        customer_privacy_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "customer_privacy"))
        )
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        save_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
        )
        save_button.click()

        # 7. Wait for the redirect after login.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
        )

        # 8. Confirm that login was successful
        # Check "Sign out" button
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
            )
            self.assertIsNotNone(sign_out_link)
            self.assertTrue(sign_out_link.is_displayed())
            self.assertIsNotNone(sign_out_link.text)
            self.assertNotEqual(sign_out_link.text, "")
            self.assertEqual("Sign out", sign_out_link.text)
        except Exception as e:
            self.fail(f"Sign out link is not present or has incorrect text. Error: {e}")

        # Check username
        try:
            username_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@class, 'account')]//span[@class='hidden-sm-down']"))
            )
            self.assertIsNotNone(username_element)
            self.assertTrue(username_element.is_displayed())
            self.assertIsNotNone(username_element.text)
            self.assertNotEqual(username_element.text, "")
            expected_username = f"{self.firstname} {self.lastname}"
            self.assertEqual(expected_username, username_element.text)

        except Exception as e:
            self.fail(f"Username link is not present or has incorrect text. Error: {e}")

if __name__ == "__main__":
    unittest.main()