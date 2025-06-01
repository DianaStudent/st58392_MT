import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait

        # Open home page and click login link
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/en/login']")))
        login_link.click()

        # Click on the "Create one here" link for registration
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Create one here")))
        register_link.click()

        # Fill the registration form
        # Gender
        gender_radio = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_radio.click()

        # First name
        firstname_input = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        firstname_input.send_keys("Test")

        # Last name
        lastname_input = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        lastname_input.send_keys("User")

        # Dynamic email
        email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_input.send_keys(f"test_{random.randint(100000, 999999)}@user.com")

        # Password
        password_input = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_input.send_keys("test@user1")

        # Birthdate
        birthday_input = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday_input.send_keys("01/01/2000")

        # Privacy policy checkbox
        privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        privacy_checkbox.click()

        # Terms and conditions checkbox
        terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        terms_checkbox.click()

        # Newsletter checkbox
        newsletter_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "newsletter")))
        newsletter_checkbox.click()

        # Submit the registration form
        save_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        save_button.click()

        # Confirm successful registration by checking "Sign out" and username appearance
        sign_out_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout")))
        self.assertIsNotNone(sign_out_button, "Sign out button not found")

        user_info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.account span")))
        self.assertIsNotNone(user_info, "User info not found")
        self.assertEqual(user_info.text.strip(), "Test User")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()