from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver 

        # Navigate to the registration page
        sign_in_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        create_account_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Create one here")))
        create_account_link.click()

        # Fill the registration form
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "customer-form")))

        driver.find_element(By.ID, "field-id_gender-1").click()

        driver.find_element(By.ID, "field-firstname").send_keys("Test")
        driver.find_element(By.ID, "field-lastname").send_keys("User")

        # Generate a random email
        random_email = f"test_{random.randint(1000, 9999)}@user.com"
        driver.find_element(By.ID, "field-email").send_keys(random_email)

        password = "test@user1"
        password_field = driver.find_element(By.ID, "field-password")
        password_field.send_keys(password)

        # Confirm password strength
        password_strength = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "password-strength-feedback"))
        )
        if "Strong" not in password_strength.text:
            self.fail("Password did not reach the required strength")

        # Terms and conditions
        driver.find_element(By.NAME, "psgdpr").click()
        driver.find_element(By.NAME, "customer_privacy").click()

        # Submit the registration form
        driver.find_element(By.XPATH, "//button[text()='Save']").click()

        # Verify registration succeeded
        sign_out_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )
        if not sign_out_link.is_displayed():
            self.fail("Sign out link not found, registration might have failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()