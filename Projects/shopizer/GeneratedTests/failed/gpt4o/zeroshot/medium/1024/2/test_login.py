from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        
        # Accept Cookies
        try:
            accept_cookies = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except:
            self.fail("Cookie consent button not found or clickable.")

        # Click on account icon
        try:
            account_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account icon not found or clickable.")

        # Click on Login link
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found or clickable.")

        # Fill in the email and password fields
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            email_field.send_keys("test2@user.com")

            password_field = driver.find_element(By.NAME, "loginPassword")
            password_field.send_keys("test**11")
        except:
            self.fail("Email or password field not found.")

        # Submit the form
        try:
            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
            login_button.click()
        except:
            self.fail("Login button not found or not clickable.")

        # Confirm successful login by checking current URL
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            self.assertIn("/my-account", driver.current_url)
        except:
            self.fail("Failed to login or redirect to /my-account.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()