import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080")  # Replace with the actual URL

    def test_login_process(self):
        driver = self.driver

        # Wait for account icon in the top navigation bar and click it
        try:
            account_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_icon.click()
        except:
            self.fail("Account icon not found or not clickable.")

        # Wait for the login link and click it
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found or not clickable.")

        # Wait for the email input field, ensure it exists, and enter email
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            if not email_input.get_attribute("placeholder"):
                self.fail("Email input field is missing placeholder attribute.")
            email_input.send_keys("test2@user.com")
        except:
            self.fail("Email input field not found or not interactable.")

        # Wait for the password input field, ensure it exists, and enter password
        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            if not password_input.get_attribute("placeholder"):
                self.fail("Password input field is missing placeholder attribute.")
            password_input.send_keys("test**11")
        except:
            self.fail("Password input field not found or not interactable.")

        # Wait for the submit button to be clickable, and click it
        try:
            submit_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']"))
            )
            submit_button.click()
        except:
            self.fail("Submit button not found or not clickable.")

        # Confirm success by checking the URL contains '/my-account'
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("/my-account")
            )
            current_url = driver.current_url
            self.assertIn("/my-account", current_url, "URL does not contain '/my-account'. Login was not successful.")
        except:
            self.fail("Login was not successful or '/my-account' was not found in URL.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()