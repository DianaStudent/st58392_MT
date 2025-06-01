from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")
        self.email = "admin@admin.com"
        self.password = "admin"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # Find the "My account" link and click it
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'My account' link: {e}")

        # Find the email field and enter the email
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_field.clear()
            email_field.send_keys(self.email)
        except Exception as e:
            self.fail(f"Could not find or interact with email field: {e}")

        # Find the password field and enter the password
        try:
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_field.clear()
            password_field.send_keys(self.password)
        except Exception as e:
            self.fail(f"Could not find or interact with password field: {e}")

        # Find the login button and click it
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not find or click login button: {e}")

        # Verify successful login by checking for the "Log out" link
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
            )
        except Exception as e:
            self.fail(f"Login failed: 'Log out' link not found: {e}")

if __name__ == "__main__":
    unittest.main()