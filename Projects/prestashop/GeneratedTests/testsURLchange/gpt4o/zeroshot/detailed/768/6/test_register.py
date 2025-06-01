import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless to avoid opening a browser window
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def generate_email(self):
        random_number = random.randint(100000, 999999)
        return f"test_{random_number}@user.com"

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage and verify page load
        try:
            assert "Popular Products" in driver.page_source
        except AssertionError:
            self.fail("Homepage did not load correctly.")

        # Step 2: Click the login link from the top navigation
        try:
            login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
            login_link.click()
        except Exception:
            self.fail("Login link not found or clickable.")

        # Step 3: On the login page, click on the register link
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            register_link.click()
        except Exception:
            self.fail("Register link not found or clickable.")

        # Step 4: Fill in the registration form using credentials
        try:
            mr_radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='id_gender'][value='1']")))
            mr_radio.click()

            firstname = driver.find_element(By.ID, "field-firstname")
            firstname.send_keys("Test")

            lastname = driver.find_element(By.ID, "field-lastname")
            lastname.send_keys("User")

            email_input = driver.find_element(By.ID, "field-email")
            email = self.generate_email()
            email_input.send_keys(email)

            password = driver.find_element(By.ID, "field-password")
            password.send_keys("test@user1")

            birthday = driver.find_element(By.ID, "field-birthday")
            birthday.send_keys("01/01/2000")
        except Exception:
            self.fail("Error accessing or interacting with registration form fields.")

        # Step 5: Tick all necessary checkboxes
        try:
            customer_privacy = driver.find_element(By.NAME, "customer_privacy")
            customer_privacy.click()

            terms_and_conditions = driver.find_element(By.NAME, "psgdpr")
            terms_and_conditions.click()

            newsletter = driver.find_element(By.NAME, "newsletter")
            newsletter.click()
        except Exception:
            self.fail("Error accessing or interacting with required checkboxes.")

        # Step 6: Submit the registration form
        try:
            save_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit")
            save_button.click()
        except Exception:
            self.fail("Error accessing or interacting with the save button.")

        # Step 7 & 8: Wait for redirection and confirm successful login
        try:
            sign_out_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            user_name_display = driver.find_element(By.CSS_SELECTOR, "span.hidden-sm-down").text
            self.assertIn("Test User", user_name_display, "User's name not visible in top navigation.")
        except Exception:
            self.fail("Failed to confirm registration and login success.")

if __name__ == '__main__':
    unittest.main()