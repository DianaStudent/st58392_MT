from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # You can replace with any other WebDriver if needed
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        try:
            # Accept cookies
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
            
            # Click account icon
            account_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_icon.click()

            # Click the "Login" link
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()

            # Fill in Email
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            email_input.send_keys("test2@user.com")

            # Fill in Password
            password_input = wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
            password_input.send_keys("test**11")

            # Submit the login form
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            login_button.click()

            # Check for redirection to my-account page
            wait.until(EC.url_contains("/my-account"))

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()