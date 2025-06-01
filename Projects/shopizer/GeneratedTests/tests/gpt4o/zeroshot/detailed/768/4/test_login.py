from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login_process(self):
        driver = self.driver
        
        # Click on the account icon/button in the top-right.
        account_icon = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_icon.click()

        # Wait for the dropdown and click the "Login" link.
        login_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        # Wait for the login form to appear.
        username_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Fill in the username field.
        username_input.clear()
        username_input.send_keys("test2@user.com")

        # Fill in the password field.
        password_input = driver.find_element(By.CLASS_NAME, "user-password")
        password_input.clear()
        password_input.send_keys("test**11")
        
        # Click the login button.
        login_button = driver.find_element(By.XPATH, "//button[@type='submit' and span='Login']")
        login_button.click()

        # Wait for redirection or page update.
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "myaccount-area"))
        )

        # Confirm successful login by verifying that the current URL contains "/my-account".
        current_url = driver.current_url
        if not "/my-account" in current_url:
            self.fail("The page did not navigate to '/my-account' as expected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()