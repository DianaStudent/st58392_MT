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
        product_elements = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        return len(product_elements)

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        tables_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Tables"))
        )
        tables_tab.click()

        # 3. Wait for product grid to update.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Tables' and contains(@class, 'active')]"))
        )

        # 4. Store number of visible products.
        tables_product_count = self.get_product_count()
        if tables_product_count == 0:
            self.fail("No products displayed after applying 'Tables' filter.")
        print(f"Number of tables products: {tables_product_count}")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh.
        chairs_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Chairs"))
        )
        chairs_tab.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs' and contains(@class, 'active')]"))
        )

        # 6. Verify that the list of products is updated and different from the previous.
        chairs_product_count = self.get_product_count()
        if chairs_product_count == 0:
            self.fail("No products displayed after applying 'Chairs' filter.")
        print(f"Number of chairs products: {chairs_product_count}")
        self.assertNotEqual(tables_product_count, chairs_product_count,
                             "Product count did not change after switching to 'Chairs' filter.")

        # 7. Then click the "All" filter to reset.
        all_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "All"))
        )
        all_tab.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='All' and contains(@class, 'active')]"))
        )

        # 8. Confirm that product list contains more items than after previous filters.
        all_product_count = self.get_product_count()
        if all_product_count == 0:
            self.fail("No products displayed after applying 'All' filter.")
        print(f"Number of all products: {all_product_count}")
        self.assertGreater(all_product_count, tables_product_count,
                             "Product count is not greater after switching to 'All' filter.")
        self.assertGreater(all_product_count, chairs_product_count,
                             "Product count is not greater after switching to 'All' filter.")

if __name__ == "__main__":
    unittest.main()