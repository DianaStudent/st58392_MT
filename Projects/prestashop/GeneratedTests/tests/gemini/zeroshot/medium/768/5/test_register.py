import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email = 'test_' + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + '@user.com'
        self.password = 'test@user1'

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        # 1. Click on the login link
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 2. Click on the registration link
        register_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
        )
        if register_link:
            register_link.click()
        else:
            self.fail("Registration link not found")

        # 3. Fill in the registration form
        # Gender
        mr_radio = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
        )
        if mr_radio:
            mr_radio.click()
        else:
            self.fail("Mr. radio button not found")

        # First name
        firstname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        if firstname_input:
            firstname_input.send_keys("Test")
        else:
            self.fail("First name input not found")

        # Last name
        lastname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        if lastname_input:
            lastname_input.send_keys("User")
        else:
            self.fail("Last name input not found")

        # Email
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        if email_input:
            email_input.send_keys(self.email)
        else:
            self.fail("Email input not found")

        # Password
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        if password_input:
            password_input.send_keys(self.password)
        else:
            self.fail("Password input not found")

        # Birthday
        birthday_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        if birthday_input:
            birthday_input.send_keys("01/01/2000")
        else:
            self.fail("Birthday input not found")

        # 4. Check required checkboxes
        # GDPR
        gdpr_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "psgdpr"))
        )
        if gdpr_checkbox:
            gdpr_checkbox.click()
        else:
            self.fail("GDPR checkbox not found")

        # Customer Privacy
        privacy_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "customer_privacy"))
        )
        if privacy_checkbox:
            privacy_checkbox.click()
        else:
            self.fail("Customer privacy checkbox not found")

        # 5. Submit the form
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found")

        # 6. Confirm success
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]"))
        )

        if sign_out_link:
            self.assertEqual("Sign out", sign_out_link.text)
        else:
            self.fail("Sign out link not found after registration")


if __name__ == "__main__":
    unittest.main()