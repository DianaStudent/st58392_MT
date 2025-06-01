import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebPageElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check the logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='logo']/a/img")))
        except:
            self.fail("Logo not found")
        
        # Check the navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links not found or not visible")
        
        # Check account setting button
        try:
            account_btn = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        except:
            self.fail("Account setting button not found")
        
        # Check login/register tab
        try:
            login_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='login']")))
            register_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register']")))
        except:
            self.fail("Login/Register tabs not found")

        # Check login form fields
        try:
            username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
        except:
            self.fail("Login form elements not found")

        # Check if forgot password link is visible
        try:
            forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot Password?")))
        except:
            self.fail("Forgot Password link not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()