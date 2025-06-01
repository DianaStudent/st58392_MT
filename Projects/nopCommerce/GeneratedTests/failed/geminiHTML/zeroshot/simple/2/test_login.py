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
        driver = self.driver
        # Navigate to login page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("Could not find 'My account' link on the home page.")

        # Find email and password fields and login button
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
        except:
            self.fail("Could not find email field, password field, or login button on the login page.")

        # Enter credentials and click login
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        login_button.click()

        # Verify successful login
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "administration"))
            )
            print("Login successful!")
        except:
            self.fail("Login failed. Could not find 'Administration' link after login.")

if __name__ == "__main__":
    unittest.main()