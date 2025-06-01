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

        # Accept cookies if present
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

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
        except:
            self.fail("Tables tab not found")

        # 3. Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//a[@href='/product/olive-table']"))
            )
        except:
            self.fail("No tables displayed after filter")

        # 4. Store number of visible products
        tables_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
        tables_count = len(tables_products)
        self.assertTrue(tables_count > 0, "No products found after filtering by Tables")

        # 5. Switch to the "Chairs" filter
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found")

        # Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//a[@href='/product/chair']"))
            )
        except:
            self.fail("No chairs displayed after filter")

        # 6. Verify that the list of products is updated and different from the previous
        chairs_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
        chairs_count = len(chairs_products)
        self.assertTrue(chairs_count > 0, "No products found after filtering by Chairs")
        self.assertNotEqual(tables_count, chairs_count, "Product count did not change after filtering")

        # 7. Then click the "All" filter to reset
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except:
            self.fail("All tab not found")

        # Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//a[@href='/product/olive-table']"))
            )
        except:
            self.fail("No products displayed after filter")

        # 8. Confirm that product list contains more items than after previous filters.
        all_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
        all_count = len(all_products)
        self.assertTrue(all_count > 0, "No products found after filtering by All")
        self.assertGreater(all_count, tables_count, "Product count after 'All' filter is not greater than 'Tables'")
        self.assertGreater(all_count, chairs_count, "Product count after 'All' filter is not greater than 'Chairs'")

if __name__ == "__main__":
    unittest.main()