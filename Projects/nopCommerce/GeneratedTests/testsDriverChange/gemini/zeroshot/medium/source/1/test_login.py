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
        # 1. Open the home page. (Done in setUp)

        # 2. Click the "My account" link.
        try:
            my_account_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'My account' link: {e}")

        # 3. Wait for the login page to load.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except Exception as e:
            self.fail(f"Login page did not load correctly: {e}")

        # 4. Enter the email and password.
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "Password"))
            )

            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to enter email or password: {e}")

        # 5. Click the login button to submit the form.
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
            )
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to click the login button: {e}")

        # 6. Verify that the user is logged in by checking the "My account" link is present in the top navigation.
        try:
            my_account_link_after_login = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            self.assertTrue(my_account_link_after_login.is_displayed())
        except Exception as e:
            self.fail(f"Login failed. 'My account' link not found after login: {e}")


if __name__ == "__main__":
    unittest.main()