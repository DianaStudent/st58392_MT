import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        
        # Step 2: Click the login link
        login_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info a"))
        )
        login_link.click()

        # Step 3: Click on the register link
        register_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here"))
        )
        register_link.click()

        # Generate a dynamic email address
        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"

        # Step 4: Fill in the registration form
        gender_mr = self.wait.until(
            EC.presence_of_element_located((By.ID, "field-id_gender-1"))
        )
        gender_mr.click()

        first_name_field = driver.find_element(By.ID, "field-firstname")
        last_name_field = driver.find_element(By.ID, "field-lastname")
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")
        birthday_field = driver.find_element(By.ID, "field-birthday")

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        email_field.send_keys(email)
        password_field.send_keys("test@user1")
        birthday_field.send_keys("01/01/2000")

        # Step 5: Tick checkboxes
        checkboxes = [
            ("optin", False), # Receive offers
            ("psgdpr", True), # Agree to terms
            ("newsletter", True), # Newsletter
            ("customer_privacy", True) # Privacy
        ]

        for checkbox_name, should_check in checkboxes:
            checkbox = driver.find_element(By.NAME, checkbox_name)
            if should_check and not checkbox.is_selected():
                checkbox.click()
            elif not should_check and checkbox.is_selected():
                checkbox.click()

        # Step 6: Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_button.click()

        # Step 7 & 8: Confirm successful login
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info .logout")))
        sign_out_button = driver.find_element(By.CSS_SELECTOR, "#_desktop_user_info .logout")
        user_name_display = driver.find_element(By.CSS_SELECTOR, "#_desktop_user_info .account span")

        self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not visible.")
        self.assertTrue(user_name_display.is_displayed(), "User name is not visible.")
        self.assertIn("Test User", user_name_display.text, "User name is not matching.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()