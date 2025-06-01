import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://localhost:8080/en/"
        self.credentials = {
            "gender": "1",
            "firstname": "Test",
            "lastname": "User",
            "password": "test@user1",
            "birthday": "01/01/2000"
        }
        self.email = "test_" + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + "@user.com"

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the homepage.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a")
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(sign_in_link_locator)
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found.")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(register_link_locator)
        )
        if register_link:
            register_link.click()
        else:
            self.fail("Registration link not found.")

        # 4. Fill in the registration form.
        gender_locator = (By.ID, "field-id_gender-1")
        gender_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(gender_locator)
        )
        if gender_element:
            gender_element.click()
        else:
            self.fail("Gender element not found.")

        firstname_locator = (By.ID, "field-firstname")
        firstname_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(firstname_locator)
        )
        if firstname_element:
            firstname_element.send_keys(self.credentials["firstname"])
        else:
            self.fail("Firstname element not found.")

        lastname_locator = (By.ID, "field-lastname")
        lastname_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(lastname_locator)
        )
        if lastname_element:
            lastname_element.send_keys(self.credentials["lastname"])
        else:
            self.fail("Lastname element not found.")

        email_locator = (By.ID, "field-email")
        email_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_locator)
        )
        if email_element:
            email_element.send_keys(self.email)
        else:
            self.fail("Email element not found.")

        password_locator = (By.ID, "field-password")
        password_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(password_locator)
        )
        if password_element:
            password_element.send_keys(self.credentials["password"])
        else:
            self.fail("Password element not found.")

        birthday_locator = (By.ID, "field-birthday")
        birthday_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(birthday_locator)
        )
        if birthday_element:
            birthday_element.send_keys(self.credentials["birthday"])
        else:
            self.fail("Birthday element not found.")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(psgdpr_locator)
        )
        if psgdpr_element:
            psgdpr_element.click()
        else:
            self.fail("psgdpr element not found.")

        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(customer_privacy_locator)
        )
        if customer_privacy_element:
            customer_privacy_element.click()
        else:
            self.fail("customer_privacy element not found.")

        # 6. Submit the registration form.
        submit_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        submit_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(submit_button_locator)
        )
        if submit_button:
            submit_button.click()
        else:
            self.fail("Submit button not found.")

        # 7. Wait for the redirect after login.

        # 8. Confirm that login was successful.
        sign_out_link_locator = (By.LINK_TEXT, "Sign out")
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(sign_out_link_locator)
        )
        if sign_out_link:
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed")
        else:
            self.fail("Sign out link not found after registration.")

        username_locator = (By.XPATH, "//div[@id='_desktop_user_info']//span")
        username_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(username_locator)
        )
        if username_element:
            self.assertEqual(self.credentials["firstname"] + " " + self.credentials["lastname"], username_element.text, "Username is incorrect")
        else:
            self.fail("Username element not found after registration.")


if __name__ == "__main__":
    unittest.main()