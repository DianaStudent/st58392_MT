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
        self.wait = WebDriverWait(self.driver, 20)

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
        # 1. Open the home page (done in setUp)

        # 2. Apply the "Tables" filter
        tables_tab_locator = (By.XPATH, "//a[@data-rb-event-key='tables']")
        tables_tab = self.wait.until(EC.presence_of_element_located(tables_tab_locator))
        tables_tab.click()

        # 3. Wait for product grid to update and check at least one product is displayed
        self.wait.until(lambda driver: self.get_product_count() > 0)
        tables_product_count = self.get_product_count()
        self.assertTrue(tables_product_count > 0, "No products displayed after applying 'Tables' filter.")

        # 4. Store number of visible products
        initial_product_count = tables_product_count

        # 5. Switch to the "Chairs" filter
        chairs_tab_locator = (By.XPATH, "//a[@data-rb-event-key='chairs']")
        chairs_tab = self.wait.until(EC.presence_of_element_located(chairs_tab_locator))
        chairs_tab.click()

        # Wait for product grid to refresh and check at least one product is displayed
        self.wait.until(lambda driver: self.get_product_count() > 0)
        chairs_product_count = self.get_product_count()
        self.assertTrue(chairs_product_count > 0, "No products displayed after applying 'Chairs' filter.")

        # 6. Verify that the list of products is updated and different from the previous.
        self.assertNotEqual(initial_product_count, chairs_product_count, "Product count did not change after switching to 'Chairs' filter.")

        # 7. Then click the "All" filter to reset
        all_tab_locator = (By.XPATH, "//a[@data-rb-event-key='all']")
        all_tab = self.wait.until(EC.presence_of_element_located(all_tab_locator))
        all_tab.click()

        # Wait for product grid to refresh and check at least one product is displayed
        self.wait.until(lambda driver: self.get_product_count() > 0)
        all_product_count = self.get_product_count()
        self.assertTrue(all_product_count > 0, "No products displayed after applying 'All' filter.")

        # 8. Confirm that product list contains more items than after previous filters.
        self.assertTrue(all_product_count > chairs_product_count, "Product count after 'All' filter is not greater than after 'Chairs' filter.")

if __name__ == "__main__":
    unittest.main()