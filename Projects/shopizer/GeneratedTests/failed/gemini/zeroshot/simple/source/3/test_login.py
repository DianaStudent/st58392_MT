from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()

            # Click account icon
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            ).click()

            # Click Login link
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            ).click()

            # Fill in username
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.send_keys("test2@user.com")

            # Fill in password
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            password_field.send_keys("test**11")

            # Click Login button
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
            ).click()

            # Check for successful login by verifying URL
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            self.assertIn("/my-account", driver.current_url)

        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()