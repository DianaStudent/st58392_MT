import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        # Wait for "My account" link to be clickable and click it
        my_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        my_account_link.click()
        
        # Wait for the login page to load completely
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "Email")))
        
        # Enter email and password
        email_input.send_keys("admin@admin.com")
        
        password_input = self.driver.find_element(By.ID, "Password")
        password_input.send_keys("admin")
        
        # Click the login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.login-button[type='submit']")
        login_button.click()
        
        # Verify that the "Log out" link is present
        try:
            logout_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            if not logout_link.is_displayed() or not logout_link.text:
                self.fail("Log out button is not displayed.")
        except:
            self.fail("Log out button is not found.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()