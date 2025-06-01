import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver

        # Open the homepage and click the login link
        login_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='login']")))
        login_link.click()

        # On the login page, click on the register link
        register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Fill in registration form
        self.fill_registration_form()

        # Submit the registration form
        submit_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        # Wait for redirect and confirm that login was successful
        sign_out_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        self.assertIsNotNone(sign_out_link, "Sign out button not found — registration may have failed.")
        
        user_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info span.hidden-sm-down")))
        self.assertTrue(user_name.text.strip().startswith("Test User"), "User name not visible — registration may have failed.")

    def fill_registration_form(self):
        driver = self.driver

        # Select gender
        gender_radio_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='field-id_gender-1']")))
        gender_radio_button.click()

        # Fill first name
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        first_name_input.send_keys("Test")

        # Fill last name
        last_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        last_name_input.send_keys("User")

        # Fill email
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_input.send_keys(f"test_{random.randint(100000,999999)}@user.com")

        # Fill password
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_input.send_keys("test@user1")

        # Fill birth date
        birthdate_input = self.wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthdate_input.send_keys("01/01/2000")

        # Tick checkboxes for privacy, terms, etc.
        privacy_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        if not privacy_checkbox.is_selected():
            privacy_checkbox.click()

        psgdpr_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        if not psgdpr_checkbox.is_selected():
            psgdpr_checkbox.click()

        newsletter_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "newsletter")))
        if not newsletter_checkbox.is_selected():
            newsletter_checkbox.click()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()