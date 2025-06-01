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
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)
        self.email = 'test_' + ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + '@user.com'

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver

        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a"))
        )
        if sign_in_link:
            sign_in_link.click()
        else:
            self.fail("Sign in link not found")

        # 3. On the login page, click on the register link (e.g. "No account? Create one here").
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here"))
        )
        if register_link:
            register_link.click()
        else:
            self.fail("Registration link not found")

        # 4. Fill in the following fields using credentials:
        #    - Gender, First name, Last name, Email, Password, Birthday
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
            self.fail("Firstname input not found")

        lastname_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-lastname"))
        )
        if lastname_input:
            lastname_input.send_keys("User")
        else:
            self.fail("Lastname input not found")

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
            password_input.send_keys("test@user1")
        else:
            self.fail("Password input not found")

        birthday_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-birthday"))
        )
        if birthday_input:
            birthday_input.send_keys("01/01/2000")
        else:
            self.fail("Birthday input not found")

        # 5. Tick checkboxes for privacy, newsletter, terms, etc.
        psgdpr_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "psgdpr"))
        )
        if psgdpr_checkbox:
            psgdpr_checkbox.click()
        else:
            self.fail("psgdpr checkbox not found")

        newsletter_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "newsletter"))
        )
        if newsletter_checkbox:
            newsletter_checkbox.click()
        else:
            print("Newsletter checkbox not found, continuing...")

        customer_privacy_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "customer_privacy"))
        )
        if customer_privacy_checkbox:
            customer_privacy_checkbox.click()
        else:
            self.fail("customer_privacy checkbox not found")

        # 6. Submit the registration form.
        save_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
        )
        if save_button:
            save_button.click()
        else:
            self.fail("Save button not found")

        # 7. Wait for the redirect after login.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "logout"))
        )

        # 8. Confirm that login was successful by checking that:
        #    - The "Sign out" button is present in the top navigation
        #    - The username (e.g. "test user") is also visible in the top navigation.
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )
        if sign_out_link:
            self.assertTrue("Sign out" in sign_out_link.text)
        else:
            self.fail("Sign out link not found after registration")

        username_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//span[contains(text(), 'Test User')]"))
        )

        if username_element:
            self.assertTrue("Test User" in username_element.text)
        else:
            self.fail("Username not found after registration")

if __name__ == "__main__":
    unittest.main()