import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page (Done in setUp)
        
        # Step 2: Click on the login link in the top menu
        sign_in = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        sign_in.click()

        # Step 3: Click on the register link on the login page
        create_account = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        create_account.click()

        # Step 4: Fill in the registration form fields
        # Gender
        gender_mr = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#field-id_gender-1")))
        gender_mr.click()

        # First name
        first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#field-firstname")))
        first_name.send_keys("Test")

        # Last name
        last_name = driver.find_element(By.CSS_SELECTOR, "#field-lastname")
        last_name.send_keys("User")

        # Email
        email = driver.find_element(By.CSS_SELECTOR, "#field-email")
        email_address = f"test_{random.randint(100000, 999999)}@user.com"
        email.send_keys(email_address)

        # Password
        password = driver.find_element(By.CSS_SELECTOR, "#field-password")
        password.send_keys("test@user1")

        # Birthday
        birthday = driver.find_element(By.CSS_SELECTOR, "#field-birthday")
        birthday.send_keys("01/01/1990")

        # Step 5: Check required checkboxes
        terms_conditions = driver.find_element(By.NAME, "psgdpr")
        if not terms_conditions.is_selected():
            terms_conditions.click()

        privacy_policy = driver.find_element(By.NAME, "customer_privacy")
        if not privacy_policy.is_selected():
            privacy_policy.click()

        # Step 6: Submit the form
        save_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-primary")))
        save_button.click()

        # Step 7: Confirm success by checking for the presence of "Sign out" in the top bar
        try:
            sign_out = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            self.assertTrue(sign_out.is_displayed(), "Sign out not displayed")
        except Exception as e:
            self.fail("Registration failed, 'Sign out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()