import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        
        # Check header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header area is not visible")

        # Check Cookie Consent Button
        try:
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie consent 'Accept' button is not visible")

        # Check Main Menu Navigation Links
        nav_links = ['/', '/category/tables', '/category/chairs']
        nav_menu = self.driver.find_element(By.CSS_SELECTOR, "nav ul")
        
        for link in nav_links:
            try:
                nav_menu.find_element(By.XPATH, f".//a[@href='{link}']")
            except:
                self.fail(f"Navigation link {link} is not present in main menu")

        # Check login and register links
        account_settings_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_settings_button.click()
        
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        except:
            self.fail("Login link is not visible")
            
        try:
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Register link is not visible")

        # Check footer subscribe input and button
        try:
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
        except:
            self.fail("Subscribe email input is not visible")
            
        try:
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
        except:
            self.fail("Subscribe button is not visible")

        # Check for 'Featured Products' section
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-area")))
        except:
            self.fail("Featured Products area is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()