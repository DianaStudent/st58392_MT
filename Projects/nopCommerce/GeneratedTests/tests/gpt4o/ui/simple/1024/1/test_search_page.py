import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not visible")

        # Verify search box
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        except:
            self.fail("Search box is not visible")

        # Verify search button
        try:
            search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Search button is not visible")

        # Verify search page title
        try:
            page_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-title h1")))
            assert page_title.text == "Search"
        except:
            self.fail("Search page title is not visible or incorrect")

        # Verify sort order dropdown
        try:
            sort_order_dropdown = self.wait.until(EC.visibility_of_element_located((By.ID, "products-orderby")))
        except:
            self.fail("Sort order dropdown is not visible")

        # Verify product grid
        try:
            product_grid = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
        except:
            self.fail("Product grid is not visible")

        # Verify product items
        try:
            product_items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))
            assert len(product_items) > 0
        except:
            self.fail("Product items are not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()