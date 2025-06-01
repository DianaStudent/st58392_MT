import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        try:
            # Accept cookies if the button exists
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            )
            cookie_button.click()
            
            # Click the account button to open the dropdown
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'account-setting-active'))
            )
            account_button.click()

            # Click the Login link from the dropdown
            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))
            )
            login_link.click()

            # Enter email address
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            email_input.send_keys("test2@user.com")

            # Enter password
            password_input = wait.until(
                EC.presence_of_element_located((By.NAME, 'loginPassword'))
            )
            password_input.send_keys("test**11")

            # Click the Login button
            login_button = driver.find_element(By.XPATH, "//button//span[text()='Login']")
            login_button.click()
            
            # Verify redirection to /my-account
            wait.until(EC.url_contains("/my-account"))
            
        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()