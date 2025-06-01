from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        # 1. Open the home page.
        # Already done in setUp

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        tables_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Wait for product grid to update.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Olive Table']"))
        )

        # 4. Store number of visible products (1 product).
        tables_product_count = self.get_product_count()
        self.assertEqual(tables_product_count, 1, "Expected 1 product after filtering by Tables")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh (3 products).
        chairs_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Chair']"))
        )

        # 6. Verify that the list of products is updated and different from the previous.
        chairs_product_count = self.get_product_count()
        self.assertEqual(chairs_product_count, 3, "Expected 3 products after filtering by Chairs")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count should be different after switching filters")

        # 7. Then click the "All" filter to reset (4 products).
        all_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Olive Table']"))
        )

        # 8. Confirm that product list contains more items than after previous filters.
        all_product_count = self.get_product_count()
        self.assertEqual(all_product_count, 4, "Expected 4 products after filtering by All")
        self.assertGreater(all_product_count, tables_product_count, "Product count should be greater after resetting filter")
        self.assertGreater(all_product_count, chairs_product_count, "Product count should be greater after resetting filter")

if __name__ == "__main__":
    unittest.main()