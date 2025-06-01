from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get('http://localhost:3000/category-a')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check for navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, 'ul.nav-level-0 li a')
        if not nav_links or len(nav_links) < 3:
            self.fail("Not all navigation links are present")

        # Check search input field visibility
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertIsNotNone(search_input, "Search input is not visible")

        # Check if the category title is visible
        category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        self.assertIsNotNone(category_title, "Category title is not visible")

        # Check if sort select is visible
        sort_select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        self.assertIsNotNone(sort_select, "Sort select is not visible")

        # Check product list visibility
        products = driver.find_elements(By.CSS_SELECTOR, '.products .product-name')
        if not products or len(products) < 2:
            self.fail("Not all products are visible")

        # Interact with a UI element (click on the first product)
        products[0].click()

        # Confirm that the page has reacted visually
        product_page = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-name')))
        self.assertIsNotNone(product_page, "Product page did not load correctly")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()