import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # 1. Open the home page. (Done in setUp)

        # 2. Click the "My account" link to navigate to the login page.
        my_account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        if my_account_link:
            my_account_link.click()
        else:
            self.fail("My account link not found.")

        # 3. Wait for the login page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
        )

        # 4. Enter the email and password.
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "Password"))
        )

        if email_input and password_input:
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        else:
            self.fail("Email or password input not found.")

        # 5. Click the login button to submit the form.
        login_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
        )
        if login_button:
            login_button.click()
        else:
            self.fail("Login button not found.")

        # 6. Verify that the user is logged in by checking the "Administration" link is present.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Administration"))
            )
        except:
            self.fail("Login failed: Administration link not found after login.")

if __name__ == "__main__":
    unittest.main()