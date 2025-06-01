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
        # Step 1: Open the home page (already done in setUp)

        # Step 2: Click the "My account" link
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'My account' link: {e}")

        # Step 3: Wait for the login page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # Step 4: Enter the email and password.
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )

            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")

        except Exception as e:
            self.fail(f"Could not find or interact with email/password fields: {e}")

        # Step 5: Click the login button to submit the form.
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the login button: {e}")

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertTrue(logout_link.is_displayed(), "Log out link is not displayed, login failed.")
        except Exception as e:
            self.fail(f"Log out link not found or not displayed after login: {e}")

if __name__ == "__main__":
    unittest.main()