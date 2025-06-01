from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to registration page
        try:
            sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()

            registration_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
            registration_link.click()
        except Exception as e:
            self.fail(f"Navigation to registration page failed: {str(e)}")

        # Fill in registration form
        try:
            gender_mr = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='id_gender'][@value='1']")))
            gender_mr.click()

            firstname = driver.find_element(By.ID, "field-firstname")
            firstname.send_keys("Test")

            lastname = driver.find_element(By.ID, "field-lastname")
            lastname.send_keys("User")

            email = driver.find_element(By.ID, "field-email")
            email.send_keys(self.generate_random_email())

            password = driver.find_element(By.ID, "field-password")
            password.send_keys("test@user1")

            customer_privacy_checkbox = driver.find_element(By.XPATH, "//input[@name='customer_privacy']")
            customer_privacy_checkbox.click()

            terms_checkbox = driver.find_element(By.XPATH, "//input[@name='psgdpr']")
            terms_checkbox.click()

            submit_button = driver.find_element(By.XPATH, "//button[text()='Save']")
            submit_button.click()
        except Exception as e:
            self.fail(f"Filling registration form failed: {str(e)}")

        # Confirm successful registration
        try:
            sign_out_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'logout')][contains(text(), 'Sign out')]")))
            self.assertIsNotNone(sign_out_text, "Registration failed: 'Sign out' text not found.")
        except Exception as e:
            self.fail(f"Confirmation of registration success failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()