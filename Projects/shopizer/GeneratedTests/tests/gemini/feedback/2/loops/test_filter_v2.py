import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Chrome()
        except AttributeError as e:
            self.fail(f"Failed to initialize Chrome driver: {e}")
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

        # Accept cookies if present
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        try:
            tables_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables tab not found")

        # 3. Wait for product grid to update.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab-pane') and contains(@class, 'active') and contains(@class, 'show')]//a[@href='/product/olive-table']"))
            )
        except:
            self.fail("Product grid did not update after applying 'Tables' filter")

        # 4. Store number of visible products (1 product).
        tables_products = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'tab-pane') and contains(@class, 'active') and contains(@class, 'show')]//div[@class='product-wrap-2 mb-25']")
        tables_product_count = len(tables_products)
        self.assertTrue(tables_product_count > 0, "No products displayed after applying 'Tables' filter")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh (3 products).
        try:
            chairs_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found")

        # Wait for product grid to update after applying "Chairs" filter
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab-pane') and contains(@class, 'active') and contains(@class, 'show')]//a[@href='/product/chair']"))
            )
        except:
            self.fail("Product grid did not update after applying 'Chairs' filter")

        # 6. Verify that the list of products is updated and different from the previous.
        chairs_products = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'tab-pane') and contains(@class, 'active') and contains(@class, 'show')]//div[@class='product-wrap-2 mb-25']")
        chairs_product_count = len(chairs_products)
        self.assertTrue(chairs_product_count > 0, "No products displayed after applying 'Chairs' filter")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after applying 'Chairs' filter")

        # 7. Then click the "All" filter to reset (4 products).
        try:
            all_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except:
            self.fail("All tab not found")

        # Wait for product grid to update after applying "All" filter
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab-pane') and contains(@class, 'active') and contains(@class, 'show')]//a[@href='/product/chair']"))
            )
        except:
            self.fail("Product grid did not update after applying 'All' filter")

        # 8. Confirm that product list contains more items than after previous filters.
        all_products = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'tab-pane') and contains(@class, 'active') and contains(@class, 'show')]//div[@class='product-wrap-2 mb-25']")
        all_product_count = len(all_products)
        self.assertTrue(all_product_count > 0, "No products displayed after applying 'All' filter")
        self.assertTrue(all_product_count > tables_product_count, "Product count did not increase after applying 'All' filter")
        self.assertTrue(all_product_count > chairs_product_count, "Product count did not increase after applying 'All' filter")

if __name__ == "__main__":
    unittest.main()