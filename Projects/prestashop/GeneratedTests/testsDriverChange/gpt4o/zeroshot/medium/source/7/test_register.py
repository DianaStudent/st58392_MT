import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Wait for the 'Sign in' link and click it
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        sign_in_link.click()

        # Wait for the 'No account? Create one here' link and click it
        create_account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here"))
        )
        create_account_link.click()

        # Fill in the registration form
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer-form"))
        )

        # Select gender
        gender_radio = driver.find_element(By.ID, "field-id_gender-1")
        gender_radio.click()

        # Enter first name
        firstname_input = driver.find_element(By.ID, "field-firstname")
        firstname_input.send_keys("Test")

        # Enter last name
        lastname_input = driver.find_element(By.ID, "field-lastname")
        lastname_input.send_keys("User")

        # Enter email
        email_input = driver.find_element(By.ID, "field-email")
        unique_email = f"test_{int(time.time())}@user.com"
        email_input.send_keys(unique_email)

        # Enter password
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        # Enter birthday
        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("01/01/2000")

        # Check required checkboxes
        gdpr_checkbox = driver.find_element(By.NAME, "psgdpr")
        gdpr_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Confirm success by checking for 'Sign out' link presence
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out_link.is_displayed(), "Sign out is not displayed")
        except:
            self.fail("Registration failed: 'Sign out' not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()