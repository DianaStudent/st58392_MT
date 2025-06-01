from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver, here using Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        
        # Locate and click the 'My account' link to navigate to the login page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail(f"Failed to locate 'My account' link: {str(e)}")
        
        # Fill in the Email and Password fields
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = driver.find_element(By.ID, "Password")
            
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except Exception as e:
            self.fail(f"Failed to locate email/password input fields: {str(e)}")
        
        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
            login_button.click()
        except Exception as e:
            self.fail(f"Failed to locate and click the login button: {str(e)}")
        
        # Confirm success by checking for the "Log out" button
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
        except Exception as e:
            self.fail(f"Login failed or 'Log out' button not found: {str(e)}")

if __name__ == "__main__":
    unittest.main()