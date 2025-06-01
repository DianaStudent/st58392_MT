from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestCategoryA(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Verify header links
            header_links = driver.find_elements(By.CSS_SELECTOR, ".primary-nav .cat-parent a")
            if not header_links:
                self.fail("Header links are missing.")
            for link in header_links:
                self.assertTrue(link.is_displayed(), "Header link is not visible.")
            
            # Verify search input
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

            # Verify product sort dropdown
            sort_dropdown = driver.find_element(By.CSS_SELECTOR, ".sort select")
            self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible.")

            # Verify products are visible
            products = driver.find_elements(By.CSS_SELECTOR, ".products .product-name")
            if not products:
                self.fail("Products are missing.")
            for product in products:
                self.assertTrue(product.is_displayed(), "Product is not visible.")
            
            # Interact with an element (click a product)
            products[0].click()
            product_page_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb .is-active a")))
            self.assertIn("Product", product_page_title.text, "Product page did not load correctly.")

        except Exception as e:
            self.fail(f"Exception occurred: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()