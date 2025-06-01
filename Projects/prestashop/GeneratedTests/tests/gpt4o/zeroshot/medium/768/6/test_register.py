import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_registration(self):
        driver = self.driver

        # Open home page and click on "Sign in"
        sign_in_link = self._wait_and_find(By.XPATH, "//span[text()='Sign in']")
        if not sign_in_link:
            self.fail("Sign in link not found on home page.")
        sign_in_link.click()

        # Click on "Create one here" on login page
        create_account_link = self._wait_and_find(By.LINK_TEXT, "No account? Create one here")
        if not create_account_link:
            self.fail("Create account link not found on login page.")
        create_account_link.click()

        # Fill the registration form
        gender_radio = self._wait_and_find(By.ID, "field-id_gender-1")
        if gender_radio:
            gender_radio.click()

        first_name = driver.find_element(By.ID, "field-firstname")
        first_name.send_keys("Test")
        
        last_name = driver.find_element(By.ID, "field-lastname")
        last_name.send_keys("User")

        email_field = driver.find_element(By.ID, "field-email")
        email_field.send_keys(f"test_{int(time.time())}@user.com")

        password_field = driver.find_element(By.ID, "field-password")
        password_field.send_keys("test@user1")

        birthday_field = driver.find_element(By.ID, "field-birthday")
        birthday_field.send_keys("01/01/1980")
        
        # Check the required checkboxes
        psgdpr_checkbox = driver.find_element(By.NAME, "psgdpr")
        psgdpr_checkbox.click()

        customer_privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        customer_privacy_checkbox.click()

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Save']")
        submit_button.click()

        # Confirm success by checking for "Sign out"
        sign_out_link = self._wait_and_find(By.XPATH, "//a/span[text()='Sign out']")
        if not sign_out_link:
            self.fail("Sign out link not found after registration, registration may have failed.")

    def _wait_and_find(self, by, value, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element if element.text.strip() else None
        except:
            return None

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()