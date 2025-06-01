import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for main header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        except:
            self.fail("Header not found or not visible")

        # Check for navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            try:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"Navigation link '{link_text}' not found or not visible")
        
        # Check for account and cart buttons
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        except:
            self.fail("Account button not found or not visible")

        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        except:
            self.fail("Cart button not found or not visible")

        # Check for product elements
        product_selectors = [
            (By.CSS_SELECTOR, '.product-wrap .product-img a[href="/product/olive-table"]'),
            (By.CSS_SELECTOR, '.product-wrap .product-img a[href="/product/chair"]'),
            (By.CSS_SELECTOR, '.product-wrap .product-img a[href="/product/chair-beige"]'),
            (By.CSS_SELECTOR, '.product-wrap .product-img a[href="/product/genuine-chair"]')
        ]

        for selector in product_selectors:
            try:
                product = wait.until(EC.visibility_of_element_located(selector))
            except:
                self.fail(f"Product element with selector '{selector}' not found or not visible")

        # Check for footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()