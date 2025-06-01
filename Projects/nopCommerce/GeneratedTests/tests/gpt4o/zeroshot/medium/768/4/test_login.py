import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Verify and click the "My Account" link
        try:
            my_account = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account.click()
        except:
            self.fail("My account link not found on the home page")
        
        # Wait for the login page to load
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-page"))
            )
        except:
            self.fail("Login page did not load properly")
        
        # Enter email and password
        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "Email"))
            )
            password_input = driver.find_element(By.ID, "Password")
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except:
            self.fail("Email or Password field not found on login page")
        
        # Click the login button
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login-button")
            login_button.click()
        except:
            self.fail("Login button not found on login page")
        
        # Verify that the Log out button is present
        try:
            logout_button = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
            self.assertTrue(logout_button.is_displayed(), "Log out button is not displayed")
        except:
            self.fail("Log out button not found, login might have failed")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()