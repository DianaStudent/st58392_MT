from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Or any other browser driver
        self.driver.get("http://max/")
        self.email = "admin@admin.com"
        self.password = "admin"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Navigate to the login page
        try:
            my_account_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("Could not find 'My account' link on the home page.")

        # Locate and fill in the email and password fields
        try:
            email_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            email_field.send_keys(self.email)
            password_field.send_keys(self.password)
        except:
            self.fail("Could not find email or password fields on the login page.")

        # Locate and click the login button
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except:
            self.fail("Could not find the login button on the login page.")

        # Verify successful login by checking for the "Administration" link
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Administration"))
            )
        except:
            self.fail("Login failed. Could not find 'Administration' link after login.")

if __name__ == "__main__":
    unittest.main()