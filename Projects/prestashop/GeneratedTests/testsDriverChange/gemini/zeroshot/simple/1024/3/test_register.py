import unittest
import time
import random
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
        self.email = f"test{random.randint(0, 100000)}@user.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        # 1. Go to Sign in page
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a"))
            )
            sign_in_link.click()
        except:
            self.fail("Could not find 'Sign in' link.")

        # 2. Go to registration page
        try:
            create_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            create_account_link.click()
        except:
            self.fail("Could not find 'No account? Create one here' link.")

        # 3. Fill registration form
        try:
            # Select social title
            mr_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Fill first name
            firstname_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")

            # Fill last name
            lastname_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")

            # Fill email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(self.email)

            # Fill password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys(self.password)

            # Check GDPR checkbox
            gdpr_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            gdpr_checkbox.click()

            # Check Customer privacy checkbox
            customer_privacy_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

            # Check Newsletter checkbox
            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "newsletter"))
            )
            newsletter_checkbox.click()

        except:
            self.fail("Could not fill the registration form.")

        # 4. Submit registration form
        try:
            save_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
            )
            save_button.click()
        except:
            self.fail("Could not submit the registration form.")

        # 5. Verify successful registration
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            sign_out_link = driver.find_element(By.LINK_TEXT, "Sign out")
            self.assertTrue(sign_out_link.is_displayed())
        except:
            self.fail("Registration failed. 'Sign out' link not found.")

if __name__ == "__main__":
    unittest.main()