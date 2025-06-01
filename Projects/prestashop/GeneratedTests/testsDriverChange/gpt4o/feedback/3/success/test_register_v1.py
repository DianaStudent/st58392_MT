import unittest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"test_{random_string}@user.com"

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage
        driver.get("http://localhost:8080/en/")

        # Step 2: Click the login link from the top navigation
        sign_in_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='login?back']")))
        self.assertTrue(sign_in_link.is_displayed(), "Sign in link not found.")
        sign_in_link.click()

        # Step 3: On the login page, click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertTrue(register_link.is_displayed(), "Register link not found.")
        register_link.click()

        # Step 4: Fill in registration fields
        gender = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender.click()

        firstname = driver.find_element(By.ID, "field-firstname")
        firstname.send_keys("Test")

        lastname = driver.find_element(By.ID, "field-lastname")
        lastname.send_keys("User")

        email = driver.find_element(By.ID, "field-email")
        email_value = self.generate_email()
        email.send_keys(email_value)

        password = driver.find_element(By.ID, "field-password")
        password.send_keys("test@user1")

        birthday = driver.find_element(By.ID, "field-birthday")
        birthday.send_keys("01/01/2000")

        # Step 5: Tick checkboxes
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        newsletter_checkbox.click()

        # Step 6: Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.assertTrue(save_button.is_displayed(), "Save button not found.")
        save_button.click()

        # Step 7: Wait for the redirect after login
        time.sleep(5)  # Simple wait for the page to reload, replace with a proper wait if possible

        # Step 8: Confirm that login was successful
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        username_display = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-info span.hidden-sm-down")))

        self.assertIn("Sign out", sign_out_link.text, "Sign out link not found.")
        self.assertIn("Test User", username_display.text, "Username not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()