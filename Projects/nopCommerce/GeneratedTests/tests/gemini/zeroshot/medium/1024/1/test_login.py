import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        email = "admin@admin.com"
        password = "admin"

        # Find and click the "My account" link to navigate to the login page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'My account' link: {e}")

        # Wait for the login page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # Enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.clear()
            email_input.send_keys(email)
        except Exception as e:
            self.fail(f"Could not find or enter email: {e}")

        # Enter password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.clear()
            password_input.send_keys(password)
        except Exception as e:
            self.fail(f"Could not find or enter password: {e}")

        # Click the login button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not find or click login button: {e}")

        # Verify successful login by checking for the "Administration" link
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Administration"))
            )
        except Exception as e:
            self.fail(f"Login failed. Could not find 'Administration' link: {e}")

if __name__ == "__main__":
    unittest.main()