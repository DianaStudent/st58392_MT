import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence(self):
        driver = self.driver
        
        # Check for the presence and visibility of the header logo
        header_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image img")))
        self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")
        
        # Check for the presence and visibility of navigation links
        nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.nav-level-0 > li > div.cat-parent > a")))
        self.assertEqual(len(nav_links), 3, "Not all primary navigation links are present")
        
        # Check for the presence and visibility of the search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.search-box input.search-input")))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        
        # Check for the presence and visibility of the category title
        category_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.category-title")))
        self.assertTrue(category_title.is_displayed(), "Category title is not visible")
        
        # Check for the presence and visibility of the sort dropdown
        sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.select select")))
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible")
        
        # Check for the presence and visibility of a product
        product = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-name")))
        self.assertTrue(product.is_displayed(), "Product is not visible")
        
        # Interact with elements: Sort products
        sort_dropdown.click()
        sort_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='-price']")))
        sort_option.click()
        
        # Verify the UI updates on sort selection
        selected_sort = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//select/option[@value='-price' and @selected='selected']")))
        self.assertTrue(selected_sort.is_displayed(), "Sort option not selected properly")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()