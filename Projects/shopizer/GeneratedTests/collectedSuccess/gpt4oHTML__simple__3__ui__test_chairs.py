from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver
        wait = self.wait
        try:
            # Check for header
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header is not present or not visible")

        # Check for main menu items
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        except:
            self.fail("Home link is not present or not visible")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        except:
            self.fail("Tables link is not present or not visible")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Chairs link is not present or not visible")

        # Check for login/register links in account settings
        try:
            account_settings_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active")))
            account_settings_button.click()
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Account settings menu or its items (Login/Register) are not present or not visible")

        # Check for cart icon
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.icon-cart")))
        except:
            self.fail("Cart icon is not present or not visible")

        # Check for footer components
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer is not present or not visible")
            
        # Check subscription box
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
        except:
            self.fail("Subscription box or its components are not present or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()