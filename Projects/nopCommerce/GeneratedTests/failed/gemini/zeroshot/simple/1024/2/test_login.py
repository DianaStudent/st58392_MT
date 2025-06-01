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

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Navigate to login page
        try:
            my_account_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("Could not find 'My account' link.")

        # Enter credentials and submit
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )

            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
            login_button.click()

        except:
            self.fail("Could not find email/password input or login button.")

        # Verify successful login
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
            )
        except:
            self.fail("Login failed: 'Log out' link not found after login.")

if __name__ == "__main__":
    unittest.main()