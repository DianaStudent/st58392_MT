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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        try:
            tables_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']")))
            tables_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Tables' tab: {e}")

        # 3. Wait for product grid to update.
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//h3/a[text()='Olive Table']")))
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'Tables' tab: {e}")

        # 4. Store number of visible products (1 product).
        tables_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
        tables_product_count = len(tables_products)
        self.assertEqual(tables_product_count, 1, "Incorrect number of products after filtering by Tables")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh (3 products).
        try:
            chairs_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']")))
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Chairs' tab: {e}")

        # Wait for product grid to update.
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//h3/a[text()='Chair']")))
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'Chairs' tab: {e}")

        # 6. Verify that the list of products is updated and different from the previous.
        chairs_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
        chairs_product_count = len(chairs_products)
        self.assertEqual(chairs_product_count, 3, "Incorrect number of products after filtering by Chairs")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after filtering")

        # 7. Then click the "All" filter to reset (4 products).
        try:
            all_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='All']")))
            all_tab.click()
        except Exception as e:
            self.fail(f"Could not find or click 'All' tab: {e}")

        # Wait for product grid to update.
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tab-pane active show']//h3/a[text()='Olive Table']")))
        except Exception as e:
            self.fail(f"Product grid did not update after clicking 'All' tab: {e}")

        # 8. Confirm that product list contains more items than after previous filters.
        all_products = driver.find_elements(By.XPATH, "//div[@class='tab-pane active show']//div[@class='product-wrap-2 mb-25']")
        all_product_count = len(all_products)
        self.assertEqual(all_product_count, 4, "Incorrect number of products after filtering by All")
        self.assertGreater(all_product_count, tables_product_count, "Product count is not greater after clicking 'All' tab")
        self.assertGreater(all_product_count, chairs_product_count, "Product count is not greater after clicking 'All' tab")

if __name__ == "__main__":
    unittest.main()