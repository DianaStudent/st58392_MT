import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/category/tables")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo img')))
        except:
            self.fail("Logo not found or not visible.")

        # Check main menu
        try:
            main_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.main-menu')))
            home_link = main_menu.find_element(By.CSS_SELECTOR, 'a[href="/"]')
            tables_link = main_menu.find_element(By.CSS_SELECTOR, 'a[href="/category/tables"]')
            chairs_link = main_menu.find_element(By.CSS_SELECTOR, 'a[href="/category/chairs"]')
        except:
            self.fail("Main menu or menu links not found or not visible.")

        # Check accept cookies button
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except:
            self.fail("Accept Cookies button not found or not visible.")

        # Check products
        try:
            products = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.shop-area .product-wrap')))
        except:
            self.fail("Products not found or not visible.")

        # Check footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer-area')))
        except:
            self.fail("Footer not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()