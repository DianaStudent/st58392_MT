import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Or any other browser you prefer
        self.driver.get("http://max/")
        self.driver.maximize_window()

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

        # Locate the email and password fields and the login button
        try:
            email_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
        except:
            self.fail("Could not find email field, password field, or login button on the login page.")

        # Enter the login credentials
        email_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        # Click the login button
        login_button.click()

        # Verify successful login by checking for the "Log out" link.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
        except:
            self.fail("Login failed. Could not find 'Log out' link after login.")

if __name__ == "__main__":
    unittest.main()