import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CategoryATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/category-a')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_category_a_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, 'header'))
        )
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer visibility
        footer = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, 'footer'))
        )
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check main category link visibility
        category_a_link = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'Category A'))
        )
        self.assertIsNotNone(category_a_link, "Category A link is not visible")

        # Check search input visibility
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'search-input'))
        )
        self.assertIsNotNone(search_input, "Search input is not visible")

        # Check products availability
        products = driver.find_elements(By.CLASS_NAME, 'product-caption')
        self.assertGreater(len(products), 0, "No products are available")

        # Check interaction with a product link
        if products:
            product_link = products[0].find_element(By.TAG_NAME, 'a')
            product_link.click()

            # Ensure that the product page is loaded
            page_title = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'category-title'))
            )
            self.assertIn("Category A", page_title.text, "Product page title is incorrect")
        
        # Check cart button visibility
        cart_button = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button'))
        )
        self.assertIsNotNone(cart_button, "Cart button is not visible")

if __name__ == '__main__':
    unittest.main()