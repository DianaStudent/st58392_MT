import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Accept Cookies
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()

            # Click account icon
            account_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
            
            # Click 'Login' link
            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Enter credentials and submit the form
            username_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )

            username_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")
            login_button.click()

            # Verify login success by checking for URL
            wait.until(
                EC.url_contains("/my-account")
            )

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()