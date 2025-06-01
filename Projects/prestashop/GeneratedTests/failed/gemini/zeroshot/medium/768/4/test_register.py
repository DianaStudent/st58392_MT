from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email = 'test_' + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + '@user.com'
        self.password = 'test@user1'

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        # 1. Click on the login link in the top menu
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 2. Click on the register link on the login page
        create_account_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
        )

        if create_account_link:
            create_account_link.click()
        else:
            self.fail("Create account link not found")

        # 3. Fill in the registration form fields
        gender_mr_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-id_gender-1"))
        )
        if gender_mr_radio:
            gender_mr_radio.click()
        else:
            self.fail("Gender radio button not found")

        firstname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-firstname"))
        )
        if firstname_input:
            firstname_input.send_keys("Test")
        else:
            self.fail("First name input not found")

        lastname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        if lastname_input:
            lastname_input.send_keys("User")
        else:
            self.fail("Last name input not found")

        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-email"))
        )
        if email_input:
            email_input.send_keys(self.email)
        else:
            self.fail("Email input not found")

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-password"))
        )
        if password_input:
            password_input.send_keys(self.password)
        else:
            self.fail("Password input not found")

        birthday_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        if birthday_input:
            birthday_input.send_keys("01/01/2000")
        else:
            self.fail("Birthday input not found")

        # 4. Check required checkboxes
        psgdpr_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "psgdpr"))
        )
        if psgdpr_checkbox:
            psgdpr_checkbox.click()
        else:
            self.fail("psgdpr checkbox not found")

        customer_privacy_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "customer_privacy"))
        )
        if customer_privacy_checkbox:
            customer_privacy_checkbox.click()
        else:
            self.fail("customer_privacy checkbox not found")

        # 5. Submit the form
        save_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
        )
        if save_button:
            save_button.click()
        else:
            self.fail("Save button not found")

        # 6. Confirm success by checking for the presence of "Sign out" in the top bar
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
        )

        if sign_out_link and sign_out_link.text == "Sign out":
            self.assertTrue(True)
        else:
            self.fail("Sign out link not found after registration")


if __name__ == "__main__":
    unittest.main()