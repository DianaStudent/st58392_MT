import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies if present
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Click the account icon
        try:
            account_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account icon not found or clickable")

        # Click the "Login" link
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found or clickable")

        # Fill in the login form
        try:
            username_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")
            username_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")
        except:
            self.fail("Login form inputs not found")

        # Submit the login form
        try:
            login_button = driver.find_element(By.XPATH, "//button[span='Login']")
            login_button.click()
        except:
            self.fail("Login button not found or clickable")

        # Check for the successful redirection
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Login failed or redirection did not happen")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()