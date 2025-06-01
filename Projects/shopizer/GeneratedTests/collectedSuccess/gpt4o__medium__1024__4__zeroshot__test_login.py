import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        # Click the accept cookies button
        try:
            cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookies_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable")

        # Open login menu
        try:
            account_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
            account_icon.click()
        except:
            self.fail("Account icon not found or not clickable")
        
        # Click Login link
        try:
            login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except:
            self.fail("Login link not found or not clickable")

        # Fill in login form
        try:
            email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            email_input.send_keys("test2@user.com")
            password_input.send_keys("test**11")
        except:
            self.fail("Login form inputs not found")

        # Submit login form
        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']")))
            login_button.click()
        except:
            self.fail("Login button not found or not clickable")
        
        # Assert successful login by checking URL
        try:
            self.wait.until(EC.url_contains("/my-account"))
        except:
            self.fail("Did not navigate to '/my-account' after login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()