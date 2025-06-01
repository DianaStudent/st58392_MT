from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
import uuid
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
        self.driver.maximize_window()
        self.email = f"test_{uuid.uuid4()}@example.com"
        self.password = "test@user1"

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        try:
            # 1. Go to Sign in page
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a"))
            )
            sign_in_link.click()

            # 2. Go to registration page
            create_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
            )
            create_account_link.click()

            # 3. Fill registration form
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "customer-form"))
            )

            # Select social title
            mr_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Fill first name
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            first_name_input.send_keys("Test")

            # Fill last name
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            last_name_input.send_keys("User")

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

            # Fill birthdate
            birthday_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "field-birthday"))
            )
            birthday_input.send_keys("01/01/2000")

            # Check the psgdpr checkbox
            psgdpr_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()

            # Check the newsletter checkbox
            newsletter_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "newsletter"))
            )
            newsletter_checkbox.click()

            # Check the customer_privacy checkbox
            customer_privacy_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

            # 4. Submit registration form
            save_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][name='submitCreate']"))
            )
            save_button.click()

            # 5. Check registration success
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
            )
            sign_out_link = driver.find_element(By.LINK_TEXT, "Sign out")
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed")

        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()