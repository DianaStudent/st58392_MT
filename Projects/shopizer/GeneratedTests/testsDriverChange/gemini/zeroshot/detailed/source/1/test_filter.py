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
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def get_product_count(self):
        product_elements = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrap-2"))
        )
        return len(product_elements)

    def test_product_filter(self):
        # 1. Open the home page (done in setUp)

        # 2. Apply the "Tables" filter
        try:
            tables_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'Tables' tab: {e}")

        # 3. Wait for product grid to update and check at least one product is displayed
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
        )
        tables_product_count = self.get_product_count()
        self.assertGreater(tables_product_count, 0, "No products displayed after applying 'Tables' filter.")

        # 4. Store number of visible products
        tables_product_count = self.get_product_count()

        # 5. Switch to the "Chairs" filter
        try:
            chairs_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'Chairs' tab: {e}")

        # Wait for grid to refresh
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
        )
        chairs_product_count = self.get_product_count()
        self.assertGreater(chairs_product_count, 0, "No products displayed after applying 'Chairs' filter.")

        # 6. Verify that the list of products is updated and different from the previous.
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after switching to 'Chairs' filter.")

        # 7. Then click the "All" filter to reset
        try:
            all_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'All' tab: {e}")

        # Wait for grid to refresh
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
        )
        all_product_count = self.get_product_count()
        self.assertGreater(all_product_count, 0, "No products displayed after applying 'All' filter.")

        # 8. Confirm that product list contains more items than after previous filters.
        self.assertGreater(all_product_count, tables_product_count, "Product count after 'All' filter is not greater than after 'Tables' filter.")
        self.assertGreater(all_product_count, chairs_product_count, "Product count after 'All' filter is not greater than after 'Chairs' filter.")

if __name__ == "__main__":
    unittest.main()