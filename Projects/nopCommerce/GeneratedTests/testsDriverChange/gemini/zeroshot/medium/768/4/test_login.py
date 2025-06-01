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
        self.email = "admin@admin.com"
        self.password = "admin"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click the "Login" link.
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
            )
            login_link.click()
        except:
            self.fail("Login link not found or not clickable.")

        # 3. Wait for the login page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except:
            self.fail("Login page did not load.")

        # 4. Enter the email and password.
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )

            email_field.send_keys(self.email)
            password_field.send_keys(self.password)

        except:
            self.fail("Email or Password field not found.")

        # 5. Click the login button to submit the form.
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except:
            self.fail("Login button not found or not clickable.")

        # 6. Verify that the user is logged in by checking the "Administration" button is present in the top navigation.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Administration"))
            )
        except:
            self.fail("Login failed. 'Administration' link not found after login.")

if __name__ == "__main__":
    unittest.main()