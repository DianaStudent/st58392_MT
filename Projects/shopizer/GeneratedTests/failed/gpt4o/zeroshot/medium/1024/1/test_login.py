from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_login(self):
        driver = self.driver
        
        try:
            # Wait for and click the account icon
            account_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_icon.click()

            # Wait for and click the "Login" link
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Wait for and fill the email field
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            email_input.send_keys("test2@user.com")

            # Fill the password field
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            password_input.send_keys("test**11")

            # Wait for and click the login button
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Login']]"))
            )
            login_button.click()

            # Check if redirected to the "/my-account" page
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            self.assertIn("/my-account", driver.current_url)

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()