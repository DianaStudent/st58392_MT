import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is not present or visible.")
        
        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is not present or visible.")
        
        # Check navigation menu
        nav_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-menu")))
        self.assertIsNotNone(nav_menu, "Main navigation menu is not present or visible.")
        
        # Click 'Login' link
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        # Check login form fields visibility
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        self.assertIsNotNone(username_field, "Username input field is not present or visible.")
        
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
        self.assertIsNotNone(password_field, "Password input field is not present or visible.")
        
        login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        self.assertIsNotNone(login_button, "Login button is not present or visible.")
        
        # Check 'Register' button in the header dropdown
        account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()
        
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_link, "Register link is not present or visible.")
        
        # Assert all necessary UI elements are present
        self.assertTrue(header.is_displayed(), "Header is not displayed.")
        self.assertTrue(footer.is_displayed(), "Footer is not displayed.")
        self.assertTrue(nav_menu.is_displayed(), "Navigation menu is not displayed.")
        self.assertTrue(username_field.is_displayed(), "Username input field is not displayed.")
        self.assertTrue(password_field.is_displayed(), "Password input field is not displayed.")
        self.assertTrue(login_button.is_displayed(), "Login button is not displayed.")
        self.assertTrue(register_link.is_displayed(), "Register link is not displayed.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()