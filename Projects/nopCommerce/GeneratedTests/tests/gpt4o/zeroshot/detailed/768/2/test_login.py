import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver

        # Wait until the Home page loads and click "My account" for login
        my_account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        my_account_link.click()

        # Wait until the login page loads
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )

        # Fill in the email and password
        email_input = driver.find_element(By.ID, "Email")
        password_input = driver.find_element(By.ID, "Password")

        if not email_input or not password_input:
            self.fail("Email or Password input field is missing.")

        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Click the login button
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        if not login_button:
            self.fail("Login button is missing.")

        login_button.click()

        # Verify that user is logged in by checking the presence of "Log out"
        log_out_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
        )
        if not log_out_button:
            self.fail("Log out button is missing. Login failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()