import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure the correct driver path
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Accept cookies button not found.")
        
        # Click the account icon
        try:
            account_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()
        except:
            self.fail("Account icon not found.")

        # Click the login link
        try:
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except:
            self.fail("Login link not found.")

        # Enter email and password
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            email_input.send_keys("test2@user.com")

            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")
        except:
            self.fail("Login form fields not found.")

        # Submit the form
        try:
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            login_button.click()
        except:
            self.fail("Login button not found.")

        # Verify login success by checking URL
        try:
            wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Login failed or '/my-account' not found in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()