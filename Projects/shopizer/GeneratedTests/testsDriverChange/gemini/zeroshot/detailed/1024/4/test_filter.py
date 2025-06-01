import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page (already done in setUp)

        # 2. Apply the "Tables" filter
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Tables' tab: {e}")

        # 3. Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']//a[@href='/product/olive-table']"))
            )
        except Exception as e:
            self.fail(f"Products not loaded after filtering by 'Tables': {e}")

        # 4. Store number of visible products
        tables_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='product-wrap-2']")
        tables_product_count = len(tables_products)
        self.assertTrue(tables_product_count > 0, "No products displayed after filtering by Tables")

        # 5. Switch to the "Chairs" filter
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Chairs' tab: {e}")

        # Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']//a[@href='/product/chair']"))
            )
        except Exception as e:
            self.fail(f"Products not loaded after filtering by 'Chairs': {e}")

        # 6. Verify that the list of products is updated and different from the previous
        chairs_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='product-wrap-2']")
        chairs_product_count = len(chairs_products)
        self.assertTrue(chairs_product_count > 0, "No products displayed after filtering by Chairs")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after filtering")

        # 7. Then click the "All" filter to reset
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'All' tab: {e}")

        # Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']//a[@href='/product/olive-table']"))
            )
        except Exception as e:
            self.fail(f"Products not loaded after filtering by 'All': {e}")

        # 8. Confirm that product list contains more items than after previous filters
        all_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'active')]//div[@class='product-wrap-2']")
        all_product_count = len(all_products)
        self.assertTrue(all_product_count > 0, "No products displayed after filtering by All")
        self.assertTrue(all_product_count > tables_product_count, "Product count not greater than after filtering by Tables")
        self.assertTrue(all_product_count > chairs_product_count, "Product count not greater than after filtering by Chairs")

if __name__ == "__main__":
    unittest.main()