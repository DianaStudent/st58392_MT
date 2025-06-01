import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://example.com/category-a")  # Replace with the actual URL

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is missing.")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is missing.")

        # Check primary navigation visibility
        primary_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
        self.assertIsNotNone(primary_nav, "Primary navigation is missing.")

        # Check search box and input visibility
        search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-box')))
        self.assertIsNotNone(search_box, "Search box is missing.")
        
        search_input = search_box.find_element(By.CLASS_NAME, 'search-input')
        self.assertIsNotNone(search_input, "Search input is missing or not visible.")

        # Check category list in navigation
        category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
        self.assertIsNotNone(category_a_link, "Category A link is missing.")
        
        subcategory_1_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 1')))
        self.assertIsNotNone(subcategory_1_link, "Subcategory 1 link is missing.")

        # Check product list
        products_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.products')))
        self.assertIsNotNone(products_section, "Products section is missing.")

        # Check product elements
        product_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product A')))
        self.assertIsNotNone(product_a, "Product A is missing.")
        
        product_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product B')))
        self.assertIsNotNone(product_b, "Product B is missing.")

        # Interact with a product
        product_a.click()

        # Confirm UI reacts visually after the click (e.g., checks title on the new page)
        new_page_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-name')))
        self.assertIsNotNone(new_page_title, "New page product title missing after clicking Product A.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()