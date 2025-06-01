import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to registration page
        try:
            sign_in_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()

            registration_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Create one here"))
            )
            registration_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to registration page: {e}")

        # Fill the registration form
        try:
            first_name = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
            last_name = driver.find_element(By.ID, "field-lastname")
            email = driver.find_element(By.ID, "field-email")
            password = driver.find_element(By.ID, "field-password")
            gender_mr = driver.find_element(By.ID, "field-id_gender-1")
            newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
            partners_checkbox = driver.find_element(By.NAME, "optin")
            terms_checkbox = driver.find_element(By.NAME, "psgdpr")
            privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")

            first_name.send_keys("Test")
            last_name.send_keys("User")
            dynamic_email = "test_" + ''.join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"
            email.send_keys(dynamic_email)
            password.send_keys("test@user1")
            gender_mr.click()
            newsletter_checkbox.click()
            partners_checkbox.click()
            terms_checkbox.click()
            privacy_checkbox.click()

            save_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Save')]")
            save_button.click()
        except Exception as e:
            self.fail(f"Failed to fill the registration form: {e}")

        # Confirm registration success
        try:
            sign_out = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out.is_displayed(), "Sign out not displayed, registration might have failed.")
        except Exception as e:
            self.fail(f"Registration test failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()