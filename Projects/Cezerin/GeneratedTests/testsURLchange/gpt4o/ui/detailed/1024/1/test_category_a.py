import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header presence and visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header not visible.")

        # Check footer presence and visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer not visible.")

        # Check navigation links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav a")))
            self.assertGreater(len(nav_links), 0, "Navigation links are missing.")
        except:
            self.fail("Navigation links not visible.")

        # Check and interact with search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
            search_input.send_keys("Test")
        except:
            self.fail("Search input field not visible.")

        # Check and interact with search button
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-search")))
            search_button.click()
        except:
            self.fail("Search button not visible.")

        # Check and interact with cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button")))
            cart_icon.click()
        except:
            self.fail("Cart icon not visible.")

        # Check for product listings
        try:
            products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .product-caption")))
            self.assertGreater(len(products), 0, "Product listings are missing.")
        except:
            self.fail("Product listings not visible.")
        
        # Verify filters
        try:
            filters = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".attribute-filter")))
            self.assertGreater(len(filters), 0, "Filters are missing.")
        except:
            self.fail("Filters not visible.")
            
        # Verify sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort select")))
            self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown not visible.")
        except:
            self.fail("Sort dropdown not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()