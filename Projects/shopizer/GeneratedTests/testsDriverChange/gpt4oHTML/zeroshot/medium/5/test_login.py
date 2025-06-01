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
        self.driver.maximize_window()

    def test_login_process(self):
        driver = self.driver
        
        # Step 1: Open the homepage.
        driver.get("http://localhost/")  # Change this to the correct URL as needed

        wait = WebDriverWait(driver, 20)
        
        # Step 2: Click the account icon in the top navigation bar.
        try:
            account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            account_icon.click()
        except Exception as e:
            self.fail(f"Account icon not found or not clickable: {str(e)}")
        
        # Step 3: Click the "Login" link.
        try:
            login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or not clickable: {str(e)}")
        
        # Step 4: Fill in the email and password fields.
        try:
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            email_field.send_keys("test2@user.com")
        except Exception as e:
            self.fail(f"Email field not found or not interactable: {str(e)}")

        try:
            password_field = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            password_field.send_keys("test**11")
        except Exception as e:
            self.fail(f"Password field not found or not interactable: {str(e)}")
        
        # Step 5: Submit the login form.
        try:
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            submit_button.click()
        except Exception as e:
            self.fail(f"Submit button not found or not clickable: {str(e)}")
        
        # Step 6: Confirm success by checking that the URL contains "/my-account"
        try:
            wait.until(EC.url_contains("/my-account"))
        except Exception as e:
            self.fail("Redirection to '/my-account' did not occur after login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()