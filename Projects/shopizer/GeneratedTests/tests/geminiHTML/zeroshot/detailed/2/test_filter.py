import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # Accept cookies
        try:
            cookie_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # 2. Apply the "Tables" filter
        tables_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='tables']")))
        tables_tab.click()

        # 3. Wait for product grid to update and check at least one product is displayed
        product_tables = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")))
        if not product_tables:
            self.fail("No products displayed after applying 'Tables' filter.")

        # 4. Store number of visible products
        products_tables = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")
        num_products_tables = len(products_tables)
        if num_products_tables == 0:
            self.fail("No products found after filtering for tables")

        # 5. Switch to the "Chairs" filter
        chairs_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='chairs']")))
        chairs_tab.click()

        # Wait for product grid to update and check at least one product is displayed
        product_chairs = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")))
        if not product_chairs:
            self.fail("No products displayed after applying 'Chairs' filter.")

        # 6. Verify that the list of products is updated and different from the previous
        products_chairs = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")
        num_products_chairs = len(products_chairs)
        if num_products_chairs == 0:
            self.fail("No products found after filtering for chairs")

        self.assertNotEqual(num_products_tables, num_products_chairs, "Product count did not change after switching to 'Chairs' filter.")

        # 7. Then click the "All" filter to reset
        all_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='all']")))
        all_tab.click()

        # Wait for product grid to update and check at least one product is displayed
        product_all = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")))
        if not product_all:
            self.fail("No products displayed after applying 'All' filter.")

        # 8. Confirm that product list contains more items than after previous filters
        products_all = self.driver.find_elements(By.XPATH, "//div[@aria-hidden='false' and contains(@class, 'tab-pane') and contains(@class, 'active')]//div[contains(@class, 'col-xl-3')]")
        num_products_all = len(products_all)
        if num_products_all == 0:
            self.fail("No products found after filtering for all")

        self.assertGreater(num_products_all, num_products_tables, "Product count after 'All' filter is not greater than after 'Tables' filter.")
        self.assertGreater(num_products_all, num_products_chairs, "Product count after 'All' filter is not greater than after 'Chairs' filter.")

if __name__ == "__main__":
    unittest.main()