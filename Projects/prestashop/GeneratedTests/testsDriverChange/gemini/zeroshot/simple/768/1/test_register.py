import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Go to the registration page
        try:
            sign_in_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()
        except:
            self.fail("Sign in link not found")

        try:
            create_account_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'registration')]"))
            )
            create_account_link.click()
        except:
            self.fail("Create account link not found")

        # 2. Fill in the registration form
        email = f"test{random.randint(1000, 9999)}@user.com"
        password = "test@user1"

        try:
            mr_radio = wait.until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()
        except:
            self.fail("Mr. radio button not found")

        try:
            firstname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")
        except:
            self.fail("First name input not found")

        try:
            lastname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")
        except:
            self.fail("Last name input not found")

        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(email)
        except:
            self.fail("Email input not found")

        try:
            password_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys(password)
        except:
            self.fail("Password input not found")

        try:
            psgdpr_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            psgdpr_checkbox.click()
        except:
            self.fail("psgdpr checkbox not found")

        try:
            customer_privacy_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()
        except:
            self.fail("customer_privacy checkbox not found")

        # 3. Submit the form
        try:
            save_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Save')]"))
            )
            save_button.click()
        except:
            self.fail("Save button not found")

        # 4. Verify successful registration
        try:
            sign_out_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue("Sign out" in sign_out_link.text)
        except:
            self.fail("Sign out link not found after registration. Registration failed.")

if __name__ == "__main__":
    unittest.main()