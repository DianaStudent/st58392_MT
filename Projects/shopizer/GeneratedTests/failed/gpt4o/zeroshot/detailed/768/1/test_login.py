from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        
    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for account icon/button to be present and click it
        account_icon = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button.account-setting-active')))
        account_icon.click()

        # Wait for Login link to be present and visible, then click
        login_link = wait.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, 'Login')))
        login_link.click()

        # Wait for username field to be present before continuing
        username_field = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'username')))
        password_field = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'loginPassword')))
        
        # Fill the login form
        username_field.send_keys('test2@user.com')
        password_field.send_keys('test**11')

        # Click the login button
        login_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()

        # Verify successful login by checking "/my-account" in URL
        wait.until(EC.url_contains('/my-account'))

        # Assert successful login URI structure
        current_url = driver.current_url
        self.assertIn('/my-account', current_url, 'Login failed, "/my-account" not in URL')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()