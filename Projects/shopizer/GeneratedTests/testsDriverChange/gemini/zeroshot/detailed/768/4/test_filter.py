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

    def test_product_filter(self):
        driver = self.driver

        # 1. Open the home page (already done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Tables' tab: {e}")

        # 3. Wait for product grid to update.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//a[@href='/product/olive-table']/img"))
            )
        except Exception as e:
            self.fail(f"Failed to wait for 'Tables' product grid to update: {e}")

        # 4. Store number of visible products (1 product).
        table_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")
        initial_table_product_count = len(table_products)

        if initial_table_product_count == 0:
            self.fail("No products displayed after applying 'Tables' filter.")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh (3 products).
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'Chairs' tab: {e}")

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//a[@href='/product/chair']/img"))
            )
        except Exception as e:
            self.fail(f"Failed to wait for 'Chairs' product grid to update: {e}")

        # 6. Verify that the list of products is updated and different from the previous.
        chair_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")
        chair_product_count = len(chair_products)

        if chair_product_count == 0:
            self.fail("No products displayed after applying 'Chairs' filter.")

        self.assertNotEqual(initial_table_product_count, chair_product_count, "Product count did not change after switching to 'Chairs' filter.")

        # 7. Then click the "All" filter to reset (4 products).
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
        except Exception as e:
            self.fail(f"Failed to find or click 'All' tab: {e}")

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//a[@href='/product/olive-table']/img"))
            )
        except Exception as e:
            self.fail(f"Failed to wait for 'All' product grid to update: {e}")

        # 8. Confirm that product list contains more items than after previous filters.
        all_products = driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")
        all_product_count = len(all_products)

        if all_product_count == 0:
            self.fail("No products displayed after applying 'All' filter.")

        self.assertGreater(all_product_count, chair_product_count, "Product count did not increase after switching to 'All' filter.")

if __name__ == "__main__":
    unittest.main()