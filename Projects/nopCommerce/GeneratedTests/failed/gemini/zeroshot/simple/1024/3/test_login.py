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
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Find the "My account" link and click it
        try:
            my_account_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("Could not find or click 'My account' link.")

        # Find the email field and enter the email
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_field.clear()
            email_field.send_keys("admin@admin.com")
        except:
            self.fail("Could not find or enter email.")

        # Find the password field and enter the password
        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_field.clear()
            password_field.send_keys("admin")
        except:
            self.fail("Could not find or enter password.")

        # Find the "Log in" button and click it
        try:
            login_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except:
            self.fail("Could not find or click 'Log in' button.")

        # Verify successful login by checking for "Log out" link
        try:
            logout_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
            )
            self.assertTrue(logout_link.is_displayed())
        except:
            self.fail("Login failed. 'Log out' link not found.")

if __name__ == "__main__":
    unittest.main()