import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIPresence(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        driver = self.driver
        driver.get('http://max/')

        # Check header elements
        header_links = [
            "/register?returnUrl=%2Fsearch%3Fq%3Dbook",
            "/login?returnUrl=%2Fsearch%3Fq%3Dbook",
            "/wishlist",
            "/cart"
        ]

        for link in header_links:
            try:
                element = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
                self.assertTrue(element.is_displayed(), f"Header link with href '{link}' is not visible.")
            except:
                self.fail(f"Header link with href '{link}' is missing or not visible.")

        # Check search form elements
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertTrue(search_box.is_displayed(), "Search box is not visible.")
        except:
            self.fail("Search box is missing or not visible.")

        try:
            search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button-1.search-box-button")))
            self.assertTrue(search_button.is_displayed(), "Search button is not visible.")
        except:
            self.fail("Search button is missing or not visible.")

        # Check footer links
        footer_links = [
            "/sitemap", "/shipping-returns", "/privacy-notice",
            "/conditions-of-use", "/about-us", "/contactus",
            "/news/rss/1", "/subscribenewsletter"  # Assuming newsletter has a subscribe form
        ]

        for link in footer_links:
            try:
                element = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
                self.assertTrue(element.is_displayed(), f"Footer link with href '{link}' is not visible.")
            except:
                self.fail(f"Footer link with href '{link}' is missing or not visible.")
        
        # Check product grid and item elements
        try:
            products_grid = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
            self.assertTrue(products_grid.is_displayed(), "Product grid is not visible.")
        except:
            self.fail("Product grid is missing or not visible.")

        # Check for at least one product item
        try:
            product_items = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item")))
            self.assertTrue(product_items.is_displayed(), "No product items are visible.")
        except:
            self.fail("Product items are missing or not visible.")
        
if __name__ == '__main__':
    unittest.main()