import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        try:
            # Accept cookies
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()

            # Click account setting button
            account_setting_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_setting_button.click()

            # Click Login link
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()

            # Fill in username
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_input.send_keys("test2@user.com")

            # Fill in password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            password_input.send_keys("test**11")

            # Click Login button
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )
            login_button.click()

            # Check if login was successful by checking the url
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
            self.assertIn("/my-account", driver.current_url)

        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()