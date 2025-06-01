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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def get_product_count(self):
        """Counts the number of visible product items."""
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        visible_count = 0
        for element in product_elements:
            if element.is_displayed():
                visible_count += 1
        return visible_count

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        tables_tab_locator = (By.XPATH, "//a[@data-rb-event-key='tables']")
        tables_tab = self.wait.until(EC.presence_of_element_located(tables_tab_locator))
        tables_tab.click()

        # 3. Wait for product grid to update.
        self.wait.until(lambda driver: self.get_product_count() > 0)

        # 4. Store number of visible products.
        tables_product_count = self.get_product_count()
        self.assertTrue(tables_product_count > 0, "No products displayed after applying 'Tables' filter.")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh.
        chairs_tab_locator = (By.XPATH, "//a[@data-rb-event-key='chairs']")
        chairs_tab = self.wait.until(EC.presence_of_element_located(chairs_tab_locator))
        chairs_tab.click()

        self.wait.until(lambda driver: self.get_product_count() > 0)

        # 6. Verify that the list of products is updated and different from the previous.
        chairs_product_count = self.get_product_count()
        self.assertTrue(chairs_product_count > 0, "No products displayed after applying 'Chairs' filter.")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after switching to 'Chairs' filter.")

        # 7. Then click the "All" filter to reset.
        all_tab_locator = (By.XPATH, "//a[@data-rb-event-key='all']")
        all_tab = self.wait.until(EC.presence_of_element_located(all_tab_locator))
        all_tab.click()

        self.wait.until(lambda driver: self.get_product_count() > 0)

        # 8. Confirm that product list contains more items than after previous filters.
        all_product_count = self.get_product_count()
        self.assertTrue(all_product_count > 0, "No products displayed after applying 'All' filter.")
        self.assertGreater(all_product_count, tables_product_count, "Product count after 'All' filter is not greater than after 'Tables' filter.")
        self.assertGreater(all_product_count, chairs_product_count, "Product count after 'All' filter is not greater than after 'Chairs' filter.")

if __name__ == "__main__":
    unittest.main()