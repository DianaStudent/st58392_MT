import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/")

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click 'Sign in' from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='login']")))
        login_link.click()

        # Step 2: Click 'Create one here'
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 3: Fill the registration form
        gender_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_mr.click()

        firstname = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        firstname.send_keys("Test")

        lastname = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        lastname.send_keys("User")

        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_field.send_keys(email)

        password = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password.send_keys("test@user1")

        birthday = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday.send_keys("01/01/2000")

        privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        privacy_checkbox.click()

        terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        terms_checkbox.click()

        newsletter_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "newsletter")))
        if not newsletter_checkbox.is_selected():
            newsletter_checkbox.click()

        # Step 5: Submit the registration form
        save_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit.float-xs-right")))
        save_button.click()

        # Step 6: Confirm successful login
        sign_out = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        if not sign_out:
            self.fail("Sign out link not found, user probably not logged in.")

        username_span = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-info .account span.hidden-sm-down")))
        self.assertIn("Test User", username_span.text, "Username not displayed or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()