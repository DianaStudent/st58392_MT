from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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

    def test_registration(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Click the login link
        login_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a")
        login_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(login_link_locator)
        )
        login_link.click()

        # 2. Click the registration link
        register_link_locator = (By.LINK_TEXT, "No account? Create one here")
        register_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(register_link_locator)
        )
        register_link.click()

        # 3. Fill in the registration form
        # Generate dynamic email
        random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
        email = f"test_{random_string}@user.com"

        # Select gender
        gender_locator = (By.ID, "field-id_gender-1")
        gender_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(gender_locator)
        )
        gender_radio.click()

        # Fill first name
        firstname_locator = (By.ID, "field-firstname")
        firstname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(firstname_locator)
        )
        firstname_input.send_keys(self.credentials["firstname"])

        # Fill last name
        lastname_locator = (By.ID, "field-lastname")
        lastname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(lastname_locator)
        )
        lastname_input.send_keys(self.credentials["lastname"])

        # Fill email
        email_locator = (By.ID, "field-email")
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(email_locator)
        )
        email_input.send_keys(email)

        # Fill password
        password_locator = (By.ID, "field-password")
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(password_locator)
        )
        password_input.send_keys(self.credentials["password"])

        # Fill birthday
        birthday_locator = (By.ID, "field-birthday")
        birthday_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(birthday_locator)
        )
        birthday_input.send_keys(self.credentials["birthday"])

        # Tick checkboxes
        psgdpr_locator = (By.NAME, "psgdpr")
        psgdpr_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(psgdpr_locator)
        )
        psgdpr_checkbox.click()

        newsletter_locator = (By.NAME, "newsletter")
        newsletter_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(newsletter_locator)
        )
        newsletter_checkbox.click()

        customer_privacy_locator = (By.NAME, "customer_privacy")
        customer_privacy_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(customer_privacy_locator)
        )
        customer_privacy_checkbox.click()

        # 4. Submit the registration form
        submit_button_locator = (By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']")
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(submit_button_locator)
        )
        submit_button.click()

        # 5. Wait for the redirect and confirm successful login
        sign_out_locator = (By.LINK_TEXT, "Sign out")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(sign_out_locator)
            )
        except:
            self.fail("Registration failed: Sign out link not found after registration.")

        sign_out_element = driver.find_element(*sign_out_locator)
        if sign_out_element and sign_out_element.text == "Sign out":
            print("Registration successful!")
        else:
            self.fail("Registration failed: Sign out link not found or text is incorrect.")

if __name__ == "__main__":
    unittest.main()