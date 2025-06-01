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
        self.base_url = "http://localhost:8080/en/"
        self.credentials = {
            "gender": "1",
            "firstname": "Test",
            "lastname": "User",
            "password": "test@user1",
            "birthday": "01/01/2000"
        }

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the homepage.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click the login link from the top navigation.
        login_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a")
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(login_link_locator)
        )
        login_link.click()

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(register_link_locator)
        )
        register_link.click()

        # 4. Fill in the registration form.
        # Generate dynamic email
        random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
        email = f"test_{random_string}@user.com"

        # Select Gender
        gender_locator = (By.ID, "field-id_gender-1")
        gender_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(gender_locator)
        )
        gender_radio.click()

        # First name
        firstname_locator = (By.ID, "field-firstname")
        firstname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(firstname_locator)
        )
        firstname_input.send_keys(self.credentials["firstname"])

        # Last name
        lastname_locator = (By.ID, "field-lastname")
        lastname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(lastname_locator)
        )
        lastname_input.send_keys(self.credentials["lastname"])

        # Email
        email_locator = (By.ID, "field-email")
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_locator)
        )
        email_input.send_keys(email)

        # Password
        password_locator = (By.ID, "field-password")
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(password_locator)
        )
        password_input.send_keys(self.credentials["password"])

        # Birthday
        birthday_locator = (By.ID, "field-birthday")
        birthday_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(birthday_locator)
        )
        birthday_input.send_keys(self.credentials["birthday"])

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        # psgdpr (Terms and conditions and the privacy policy)
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(psgdpr_locator)
        )
        psgdpr_checkbox.click()

        # customer_privacy (Customer data privacy)
        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(customer_privacy_locator)
        )
        customer_privacy_checkbox.click()

        # 6. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(submit_button_locator)
        )
        submit_button.click()

        # 7. Wait for the redirect after login.
        WebDriverWait(driver, 20).until(
            EC.url_contains(self.base_url)
        )

        # 8. Confirm that login was successful.
        # Check that "Sign out" button is present
        sign_out_locator = (By.LINK_TEXT, "Sign out")
        try:
            sign_out_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(sign_out_locator)
            )
            self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not displayed.")
        except:
            self.fail("Sign out button not found after registration.")

        # Check that the username is visible
        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//span")
        try:
            username_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(username_locator)
            )
            username = username_element.text
            self.assertEqual(self.credentials["firstname"] + " " + self.credentials["lastname"], username, "Incorrect username displayed.")
        except:
            self.fail("Username not found after registration.")

if __name__ == "__main__":
    unittest.main()