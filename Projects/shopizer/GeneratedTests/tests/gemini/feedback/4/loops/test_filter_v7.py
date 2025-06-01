import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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
        driver = self.driver

        # 1. Open the home page (done in setUp)

        # 2. Apply the "Tables" filter
        try:
            tables_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='tables']"))
            )
            tables_tab.click()
        except:
            self.fail("Tables tab not found")

        # 3. Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']/div[contains(@class, 'active') and contains(@class, 'show') and contains(@class, 'fade')]//div[@class='product-wrap-2']"))
            )
        except:
            self.fail("No products displayed after applying Tables filter")

        # 4. Store number of visible products
        products_tables = driver.find_elements(By.XPATH, "//div[@class='tab-content']/div[contains(@class, 'active') and contains(@class, 'show') and contains(@class, 'fade')]//div[@class='product-wrap-2']")
        num_products_tables = len(products_tables)
        if num_products_tables == 0:
            self.fail("No products found after filtering by Tables")

        # Get the product names for tables
        product_names_tables = [product.find_element(By.XPATH, ".//h3/a").text for product in products_tables]

        # 5. Switch to the "Chairs" filter
        try:
            chairs_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='chairs']"))
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found")

        # Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']/div[contains(@class, 'active') and contains(@class, 'show') and contains(@class, 'fade')]//div[@class='product-wrap-2']"))
            )
        except:
            self.fail("No products displayed after applying Chairs filter")

        # 6. Verify that the list of products is updated and different from the previous
        products_chairs = driver.find_elements(By.XPATH, "//div[@class='tab-content']/div[contains(@class, 'active') and contains(@class, 'show') and contains(@class, 'fade')]//div[@class='product-wrap-2']")
        num_products_chairs = len(products_chairs)
        if num_products_chairs == 0:
            self.fail("No products found after filtering by Chairs")

        # Get the product names for chairs
        product_names_chairs = [product.find_element(By.XPATH, ".//h3/a").text for product in products_chairs]

        # Check if the product names are different
        self.assertNotEqual(set(product_names_tables), set(product_names_chairs), "Product names did not change after switching to Chairs filter")

        # 7. Then click the "All" filter to reset
        try:
            all_tab = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-rb-event-key='all']"))
            )
            all_tab.click()
        except:
            self.fail("All tab not found")

        # Wait for product grid to update and check at least one product is displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='tab-content']/div[contains(@class, 'active') and contains(@class, 'show') and contains(@class, 'fade')]//div[@class='product-wrap-2']"))
            )
        except:
            self.fail("No products displayed after applying All filter")

        # 8. Confirm that product list contains more items than after previous filters
        products_all = driver.find_elements(By.XPATH, "//div[@class='tab-content']/div[contains(@class, 'active') and contains(@class, 'show') and contains(@class, 'fade')]//div[@class='product-wrap-2']")
        num_products_all = len(products_all)
        if num_products_all == 0:
            self.fail("No products found after filtering by All")

        self.assertGreater(num_products_all, num_products_tables, "Product count is not greater after switching to All filter compared to Tables filter")
        self.assertGreater(num_products_all, num_products_chairs, "Product count is not greater after switching to All filter compared to Chairs filter")

if __name__ == "__main__":
    unittest.main()