import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import uuid

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Go to the Sign-in page
        try:
            sign_in_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign in')]"))
            )
            sign_in_link.click()
        except:
            self.fail("Sign-in link not found")

        # 2. Go to the registration page
        try:
            create_account_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'No account? Create one here')]"))
            )
            create_account_link.click()
        except:
            self.fail("Create account link not found")

        # 3. Fill in the registration form
        try:
            # Generate a unique email address
            unique_id = str(uuid.uuid4())
            email = f"testuser_{unique_id}@example.com"

            # Select social title (Mr.)
            mr_radio = wait.until(
                EC.element_to_be_clickable((By.ID, "field-id_gender-1"))
            )
            mr_radio.click()

            # Enter first name
            firstname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-firstname"))
            )
            firstname_input.send_keys("Test")

            # Enter last name
            lastname_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-lastname"))
            )
            lastname_input.send_keys("User")

            # Enter email
            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-email"))
            )
            email_input.send_keys(email)

            # Enter password
            password_input = wait.until(
                EC.presence_of_element_located((By.ID, "field-password"))
            )
            password_input.send_keys("test@user1")

            # Check the GDPR checkbox
            gdpr_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "psgdpr"))
            )
            gdpr_checkbox.click()

            # Check the customer_privacy checkbox
            customer_privacy_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "customer_privacy"))
            )
            customer_privacy_checkbox.click()

            # Check the newsletter checkbox
            newsletter_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "newsletter"))
            )
            newsletter_checkbox.click()

            # Check the optin checkbox
            optin_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "optin"))
            )
            optin_checkbox.click()

        except Exception as e:
            self.fail(f"Error filling the form: {e}")

        # 4. Submit the form
        try:
            save_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(.,'Save')]"))
            )
            save_button.click()
        except:
            self.fail("Save button not found")

        # 5. Verify successful registration
        try:
            wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Sign out')]"))
            )
            
            account_name = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'account')]//span[contains(., 'Test User')]"))
            )

        except:
            self.fail("Sign out link not found after registration")

if __name__ == "__main__":
    unittest.main()