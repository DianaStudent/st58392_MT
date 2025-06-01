import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # 1. Open the home page. (Already done in setUp)

        # 2. Click the "My account" button in the top navigation.
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'My account' link: {e}")

        # 3. Wait until the login page loads fully.
        try:
            login_page_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
            self.assertTrue(login_page_title.is_displayed(), "Login page did not load.")
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # 4. Fill in the email and password fields using the provided credentials.
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
            self.fail(f"Failed to fill in email/password fields: {e}")

        # 5. Click the login button.
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to click login button: {e}")

        # 6. Verify that the user is logged in by checking the "My account" button is present in the top navigation.
        try:
            my_account_link_after_login = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )

            self.assertTrue(my_account_link_after_login.is_displayed(), "Login failed. 'My account' link not found after login.")

        except Exception as e:
            self.fail(f"Login verification failed: {e}")

if __name__ == "__main__":
    unittest.main()