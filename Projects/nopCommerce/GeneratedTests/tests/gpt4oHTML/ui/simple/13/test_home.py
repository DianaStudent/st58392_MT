import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header-links')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Log in')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Wishlist')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shopping cart')))
        except:
            self.fail("Header elements are missing or not visible.")

        # Check main menu
        try:
            top_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.top-menu.notmobile')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home page')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'New products')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Search')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My account')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Blog')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact us')))
        except:
            self.fail("Main menu elements are missing or not visible.")

        # Check search box
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-search-box-form')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'q')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.search-box-button')))
        except:
            self.fail("Search box elements are missing or not visible.")

        # Check footer elements
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.footer')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.footer-upper')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sitemap')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Privacy notice')))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact us')))
        except:
            self.fail("Footer elements are missing or not visible.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()