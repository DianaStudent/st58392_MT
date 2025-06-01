import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    URL = "http://localhost:8080/en/"
    EMAIL = "test@user.com"
    PASSWORD = "test@user1"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Open the homepage.
        # Already done in setUp

        # 2. Click the login link from the top navigation.
        sign_in_link_locator = (By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]")
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(sign_in_link_locator)
            )
            sign_in_link.click()
        except Exception as e:
            self.fail(f"Could not find or click sign-in link: {e}")

        # 3. Wait for the login page to load.
        email_field_locator = (By.ID, "field-email")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(email_field_locator)
            )
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # 4. Fill in the email and password fields.
        email_field = driver.find_element(*email_field_locator)
        password_field = driver.find_element(By.ID, "field-password")
        email_field.send_keys(self.EMAIL)
        password_field.send_keys(self.PASSWORD)

        # 5. Click the submit button.
        submit_button_locator = (By.ID, "submit-login")
        try:
            submit_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(submit_button_locator)
            )
            submit_button.click()
        except Exception as e:
            self.fail(f"Could not find or click submit button: {e}")

        # 6. Wait for the redirect after login.
        sign_out_link_locator = (By.XPATH, "//a[contains(@class, 'logout')]")
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(sign_out_link_locator)
            )
        except Exception as e:
            self.fail(f"Login redirect did not happen correctly: {e}")

        # 7. Confirm that login was successful.
        #   - The "Sign out" button is present in the top navigation
        #   - The username (e.g. "test user") is also visible in the top navigation.
        try:
            sign_out_link = driver.find_element(*sign_out_link_locator)
            self.assertIsNotNone(sign_out_link, "Sign out link is missing.")
            self.assertEqual(sign_out_link.text, "Sign out", "Sign out link text is incorrect.")

            user_name_locator = (By.XPATH, "//a[contains(@class, 'account')]//span")
            user_name_element = driver.find_element(*user_name_locator)
            self.assertIsNotNone(user_name_element, "User name element is missing.")
            self.assertNotEqual(user_name_element.text, "", "User name is empty.")

        except Exception as e:
            self.fail(f"Login confirmation failed: {e}")

if __name__ == "__main__":
    unittest.main()