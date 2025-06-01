import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
            self.assertTrue(header.is_displayed(), "Header is not displayed")
        except:
            self.fail("Header not found or is not visible")

        # Check main menu
        try:
            main_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.main-menu')))
            self.assertTrue(main_menu.is_displayed(), "Main menu is not displayed")

            # Verify menu items
            home_link = driver.find_element(By.LINK_TEXT, "Home")
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")

            self.assertTrue(home_link.is_displayed(), "Home link is not displayed")
            self.assertTrue(tables_link.is_displayed(), "Tables link is not displayed")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not displayed")
        except:
            self.fail("Main menu or its links not found or are not visible")

        # Check login and register links
        try:
            login_link = driver.find_element(By.LINK_TEXT, "Login")
            register_link = driver.find_element(By.LINK_TEXT, "Register")
            
            self.assertTrue(login_link.is_displayed(), "Login link is not displayed")
            self.assertTrue(register_link.is_displayed(), "Register link is not displayed")
        except:
            self.fail("Login or Register link not found or is not visible")
        
        # Check acceptance of cookies button
        try:
            cookies_btn = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertTrue(cookies_btn.is_displayed(), "Cookies button is not displayed")
        except:
            self.fail("Cookies accept button not found or is not visible")
        
        # Check presence of footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
            self.assertTrue(footer.is_displayed(), "Footer is not displayed")
        except:
            self.fail("Footer not found or is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()