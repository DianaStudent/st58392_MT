import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = "http://localhost:8080/en/"

    def generate_email(self):
        return f"test_{random.randint(100000, 999999)}@user.com"

    def test_registration_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Click on the login link in the top menu
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#_desktop_user_info a"))
        )
        login_link.click()

        # Step 2: Click on the register link on the login page
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here"))
        )
        register_link.click()

        # Step 3: Fill in the registration form fields
        email = self.generate_email()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer-form"))
        )

        driver.find_element(By.ID, "field-id_gender-1").click()
        driver.find_element(By.ID, "field-firstname").send_keys("Test")
        driver.find_element(By.ID, "field-lastname").send_keys("User")
        driver.find_element(By.ID, "field-email").send_keys(email)
        driver.find_element(By.ID, "field-password").send_keys("test@user1")
        driver.find_element(By.ID, "field-birthday").send_keys("01/01/2000")

        # Check required checkboxes
        driver.find_element(By.NAME, "psgdpr").click()
        driver.find_element(By.NAME, "customer_privacy").click()

        # Step 4: Submit the form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Step 5: Confirm success by checking for "Sign out" presence
        try:
            sign_out_text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout"))
            )
            self.assertTrue("Sign out" in sign_out_text.text)
        except Exception:
            self.fail("Registration failed, 'Sign out' not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()