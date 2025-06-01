from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")  # replace with the actual URL

    def test_login_process(self):
        driver = self.driver

        # Wait for 'My account' link and click it
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"My account link not found or not clickable: {str(e)}")

        # Wait for the email input field and enter the email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys("admin@admin.com")
        except Exception as e:
            self.fail(f"Email input not found: {str(e)}")

        # Wait for the password input field and enter the password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Password input not found: {str(e)}")

        # Wait for and click the 'Log in' button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Log in button not found or not clickable: {str(e)}")

        # Verify login by checking for the presence of the 'Log out' link
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
            )
        except Exception as e:
            self.fail(f"Log out link not found after login: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()