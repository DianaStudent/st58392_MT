import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter_process(self):
        driver = self.driver
        wait = self.wait

        # Search for "book"
        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.send_keys("book")
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # Verify that search has completed by checking for the presence of search results
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))

        # Navigate with a price filter
        driver.get("http://max/?price=0-25")

        # Verify that the product grid is updated by checking the presence of expected product items
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))
        
        products = product_grid.find_elements(By.CLASS_NAME, "item-box")
        expected_product_ids = {"4"}  # Product with a price between 0 and 25
        actual_product_ids = {product.get_attribute("data-productid") for product in products}

        if not expected_product_ids <= actual_product_ids:
            self.fail(f"Expected product IDs {expected_product_ids} not found in the results.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()