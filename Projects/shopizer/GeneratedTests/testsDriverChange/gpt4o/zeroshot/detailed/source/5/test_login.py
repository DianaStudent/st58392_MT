import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.presence_of_element_located((By.ID, 'rcc-confirm-button'))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click the accept cookies button: {e}")

        # Click on account icon
        try:
            account_icon = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.account-setting-active'))
            )
            account_icon.click()
        except Exception as e:
            self.fail(f"Failed to find or click the account icon: {e}")

        # Click on the 'Login' link
        try:
            login_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Login'))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click the login link: {e}")

        # Wait for login form and fill in credentials
        try:
            username_input = wait.until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password_input = wait.until(
                EC.presence_of_element_located((By.NAME, 'loginPassword'))
            )

            username_input.send_keys('test2@user.com')
            password_input.send_keys('test**11')

            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to fill or submit the login form: {e}")

        # Verify successful login
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.user-profile')))
            current_url = driver.current_url
            self.assertIn("/my-account", current_url)
        except Exception as e:
            self.fail(f"Failed to verify successful login: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()