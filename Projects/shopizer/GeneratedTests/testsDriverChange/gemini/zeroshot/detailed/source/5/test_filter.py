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
        """Counts the number of visible product elements."""
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        visible_count = 0
        for element in product_elements:
            if element.is_displayed():
                visible_count += 1
        return visible_count

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page (done in setUp)

        # 2. Apply the "Tables" filter
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'Tables' tab: {e}")

        # 3. Wait for product grid to update and check that at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                lambda driver: self.get_product_count() > 0
            )
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'Tables': {e}")

        # 4. Store number of visible products
        tables_product_count = self.get_product_count()
        self.assertGreater(tables_product_count, 0, "No products displayed after filtering by Tables")

        # 5. Switch to the "Chairs" filter
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'Chairs' tab: {e}")

        # Wait for product grid to update and check that at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                lambda driver: self.get_product_count() > 0
            )
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'Chairs': {e}")

        # 6. Verify that the list of products is updated and different from the previous
        chairs_product_count = self.get_product_count()
        self.assertGreater(chairs_product_count, 0, "No products displayed after filtering by Chairs")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after switching filters")

        # 7. Then click the "All" filter to reset
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='All']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not click 'All' tab: {e}")

        # Wait for product grid to update and check that at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                lambda driver: self.get_product_count() > 0
            )
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'All': {e}")

        # 8. Confirm that product list contains more items than after previous filters
        all_product_count = self.get_product_count()
        self.assertGreater(all_product_count, 0, "No products displayed after clicking All")
        self.assertGreater(all_product_count, tables_product_count, "Product count after 'All' filter is not greater than after 'Tables' filter")
        self.assertGreater(all_product_count, chairs_product_count, "Product count after 'All' filter is not greater than after 'Chairs' filter")

if __name__ == "__main__":
    unittest.main()