import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is available in your PATH
        self.driver.maximize_window()
        self.driver.get("http://max")  # Adjust to your base URL

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to login page
        my_account = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        my_account.click()

        # Verify login page loaded by checking form elements and title
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
            login_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-button")))
        except:
            self.fail("Login page did not load correctly.")

        # Input credentials and log in
        email_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")
        login_button.click()

        # Confirm successful login by checking for "Administration" link after login
        try:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Administration")))
        except:
            self.fail("Login failed - 'Administration' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()