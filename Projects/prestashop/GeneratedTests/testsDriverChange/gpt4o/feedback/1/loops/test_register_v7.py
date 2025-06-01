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
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

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
        
        # Gender
        gender_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_mr.click()

        # First name
        firstname = driver.find_element(By.ID, "field-firstname")
        firstname.send_keys("Test")

        # Last name
        lastname = driver.find_element(By.ID, "field-lastname")
        lastname.send_keys("User")

        # Generate dynamic email
        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"
        email_field = driver.find_element(By.ID, "field-email")
        email_field.send_keys(email)

        # Password
        password = driver.find_element(By.ID, "field-password")
        password.send_keys("test@user1")

        # Birthday
        birthday = driver.find_element(By.ID, "field-birthday")
        birthday.send_keys("01/01/2000")

        # Step 4: Tick checkboxes
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        # Optionally:
        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        if not newsletter_checkbox.is_selected():
            newsletter_checkbox.click()

        # Step 5: Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary form-control-submit float-xs-right']")
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