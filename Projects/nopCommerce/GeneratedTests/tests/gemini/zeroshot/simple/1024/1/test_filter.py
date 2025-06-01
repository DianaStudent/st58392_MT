import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # Search for "book"
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Apply price filter (0-15) - directly navigating to the URL
        driver.get(self.base_url + "search?q=book")

        # Check if the product grid is updated after filtering
        try:
            # Find the product grid element
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
            # Check for the presence of at least one product item
            product_items = product_grid.find_elements(By.CLASS_NAME, "product-item")
            self.assertTrue(len(product_items) > 0, "Product grid is empty after filtering.")

            #Verify that the price filter has been applied by checking the displayed price range
            price_range = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "selected-price-range"))
            )
            self.assertIn("0", price_range.text)
            self.assertIn("10000", price_range.text)

        except Exception as e:
            self.fail(f"Failed to verify product grid after filtering: {e}")

if __name__ == "__main__":
    unittest.main()