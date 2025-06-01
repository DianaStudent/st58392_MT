import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_main_ui_components(self):
        driver = self.driver

        # Check header logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
        except:
            self.fail("Logo not found or visible.")
        
        # Check cookie consent button
        try:
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie consent button not found or visible.")

        # Check language dropdown
        try:
            language_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "same-language-currency.language-style")))
        except:
            self.fail("Language dropdown not found or visible.")
        
        # Check main menu links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Main menu links not found or visible.")

        # Check login button presence
        try:
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[./i[@class='pe-7s-user-female']]")))
        except:
            self.fail("Login button not found or visible.")

        # Check elements in the login form
        driver.get("http://localhost/login")
        
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "user-password")))
            login_submit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        except:
            self.fail("Login form components not found or visible.")

        # Check elements in the register form
        driver.get("http://localhost/register")
        
        try:
            register_email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            register_password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            register_repeat_password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            register_submit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        except:
            self.fail("Register form components not found or visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()