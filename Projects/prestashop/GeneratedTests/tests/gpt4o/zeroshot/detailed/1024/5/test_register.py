import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        return f"test_{random.randint(100000, 999999)}@user.com"

    def test_registration_process(self):
        driver = self.driver
        wait = self.wait

        # Click the 'Sign in' link
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Click the 'Create account' link
        create_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        create_account_link.click()

        # Fill registration form
        wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "field-firstname"))).send_keys("Test")
        wait.until(EC.presence_of_element_located((By.ID, "field-lastname"))).send_keys("User")
        wait.until(EC.presence_of_element_located((By.ID, "field-email"))).send_keys(self.generate_email())
        wait.until(EC.presence_of_element_located((By.ID, "field-password"))).send_keys("test@user1")
        wait.until(EC.presence_of_element_located((By.ID, "field-birthday"))).send_keys("01/01/2000")

        # Check required checkboxes
        wait.until(EC.presence_of_element_located((By.NAME, "optin"))).click()
        wait.until(EC.presence_of_element_located((By.NAME, "psgdpr"))).click()
        wait.until(EC.presence_of_element_located((By.NAME, "newsletter"))).click()
        wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy"))).click()

        # Submit the form
        submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        # Verify login by checking "Sign out" visibility
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        username_display = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.account span.hidden-sm-down")))

        if not sign_out_link or sign_out_link.text.strip() == "":
            self.fail("Sign out link is not present or not visible.")

        if not username_display or username_display.text.strip().lower() != "test user":
            self.fail("Username is not displayed correctly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()