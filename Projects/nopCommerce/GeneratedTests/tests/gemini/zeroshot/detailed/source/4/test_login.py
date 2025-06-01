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
        self.email = "admin@admin.com"
        self.password = "admin"

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click the "My account" button in the top navigation.
        my_account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        if my_account_link:
            my_account_link.click()
        else:
            self.fail("My account link not found")

        # 3. Wait until the login page loads fully.
        login_page_title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1[text()='Welcome, Please Sign In!']"))
        )

        if not login_page_title:
             self.fail("Login page title not found.")

        # 4. Fill in the email and password fields using the provided credentials.
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Password"))
        )

        if email_input and password_input:
            email_input.send_keys(self.email)
            password_input.send_keys(self.password)
        else:
            self.fail("Email or Password input field not found")

        # 5. Click the login button.
        login_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
        )
        if login_button:
            login_button.click()
        else:
            self.fail("Login button not found")

        # 6. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        logout_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
        )
        if logout_link:
            self.assertTrue(logout_link.is_displayed(), "Log out link is not displayed")
        else:
            self.fail("Log out link not found after login")

if __name__ == "__main__":
    unittest.main()