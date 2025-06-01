import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header not found or not visible.")

        # Main navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Main navigation links not found or not visible.")

        # Footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer not found or not visible.")
        
        # Cookie consent button
        try:
            cookie_accept_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie accept button not found or not visible.")

        # Login form (as it's the default displayed content)
        try:
            login_username = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            login_password = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "user-password")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span[text()='Login']]")))
        except:
            self.fail("Login form elements not found or not visible.")

        # Register form link
        try:
            register_tab = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Register form link not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()