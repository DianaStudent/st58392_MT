import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver

        # Click on "My account" link to navigate to login page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("Failed to find or click the 'My account' link")

        # Enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            email_input.send_keys("admin@admin.com")
        except:
            self.fail("Failed to find or interact with email input field")

        # Enter password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )
            password_input.send_keys("admin")
        except:
            self.fail("Failed to find or interact with password input field")

        # Click on login button
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.login-button"))
            )
            login_button.click()
        except:
            self.fail("Failed to find or click the login button")

        # Confirm login by checking presence of "Log out" button
        try:
            logout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertTrue(logout_button.is_displayed(), "Log out button is not displayed")
        except:
            self.fail("Log in failed, 'Log out' button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()