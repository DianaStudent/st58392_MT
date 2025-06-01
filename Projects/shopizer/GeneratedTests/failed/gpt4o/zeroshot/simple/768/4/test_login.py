from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        
        try:
            # Accept cookies
            cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookies_button.click()

            # Click account icon
            account_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()

            # Click Login link
            login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()

            # Enter email address
            email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            email_input.send_keys("test2@user.com")

            # Enter password
            password_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
            password_input.send_keys("test**11")

            # Click Login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']/span[text()='Login']")))
            login_button.click()

            # Verify login success by checking URL
            self.wait.until(EC.url_contains("/my-account"))

        except TimeoutException:
            self.fail("Element not found or action could not be completed in time")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()