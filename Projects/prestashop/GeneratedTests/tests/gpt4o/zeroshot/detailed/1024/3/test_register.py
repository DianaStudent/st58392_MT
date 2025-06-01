import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 2: Click the login link from the top navigation
        sign_in_button = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        sign_in_button.click()

        # Step 3: On the login page, click on the register link
        register_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Create one here')]"))
        )
        register_link.click()

        # Step 4: Fill in the registration form
        gender = wait.until(
            EC.presence_of_element_located((By.ID, "field-id_gender-1"))
        )
        gender.click()
        
        first_name = driver.find_element(By.ID, "field-firstname")
        last_name = driver.find_element(By.ID, "field-lastname")
        email = driver.find_element(By.ID, "field-email")
        password = driver.find_element(By.ID, "field-password")
        birthday = driver.find_element(By.ID, "field-birthday")
        first_name.send_keys("Test")
        last_name.send_keys("User")

        # Generate dynamic email
        random_number = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email_address = f"test_{random_number}@user.com"
        email.send_keys(email_address)

        password.send_keys("test@user1")
        birthday.send_keys("01/01/2000")

        # Step 5: Tick checkboxes
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        privacy_checkbox.click()
        newsletter_checkbox.click()
        terms_checkbox.click()

        # Step 6: Submit the registration form
        submit_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-control-submit"))
        )
        submit_button.click()

        # Step 7 & 8: Confirm successful login
        sign_out_button = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )

        if not sign_out_button:
            self.fail("Sign out button is not present. Registration might have failed.")

        username_displayed = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Test User"))
        )

        if not username_displayed:
            self.fail("Username is not displayed. Registration might have failed.")

if __name__ == "__main__":
    unittest.main()