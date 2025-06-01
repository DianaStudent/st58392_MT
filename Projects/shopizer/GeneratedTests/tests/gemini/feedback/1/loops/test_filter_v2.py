import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            ).click()
        except:
            pass

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Apply the "Tables" filter by clicking the corresponding tab.
        tables_tab_locator = (By.XPATH, "//a[text()='Tables']")
        try:
            tables_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(tables_tab_locator)
            )
            tables_tab.click()
        except:
            self.fail("Tables tab not found")

        # 3. Wait for product grid to update.
        product_locator = (By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_locator)
            )
        except:
            self.fail("Product grid did not update after applying 'Tables' filter")

        # 4. Store number of visible products.
        products = self.driver.find_elements(*product_locator)
        tables_product_count = len(products)
        self.assertTrue(tables_product_count > 0, "No products displayed after applying 'Tables' filter")

        # 5. Switch to the "Chairs" filter and wait for grid to refresh.
        chairs_tab_locator = (By.XPATH, "//a[text()='Chairs']")
        try:
            chairs_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(chairs_tab_locator)
            )
            chairs_tab.click()
        except:
            self.fail("Chairs tab not found")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_locator)
            )
        except:
            self.fail("Product grid did not update after applying 'Chairs' filter")

        products = self.driver.find_elements(*product_locator)
        chairs_product_count = len(products)
        self.assertTrue(chairs_product_count > 0, "No products displayed after applying 'Chairs' filter")

        # 6. Verify that the list of products is updated and different from the previous.
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after switching to 'Chairs' filter")

        # 7. Then click the "All" filter to reset.
        all_tab_locator = (By.XPATH, "//a[text()='All']")
        try:
            all_tab = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(all_tab_locator)
            )
            all_tab.click()
        except:
            self.fail("All tab not found")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_locator)
            )
        except:
            self.fail("Product grid did not update after applying 'All' filter")

        products = self.driver.find_elements(*product_locator)
        all_product_count = len(products)
        self.assertTrue(all_product_count > 0, "No products displayed after applying 'All' filter")

        # 8. Confirm that product list contains more items than after previous filters.
        self.assertTrue(all_product_count > tables_product_count, "Product count after 'All' filter is not greater than 'Tables' filter")
        self.assertTrue(all_product_count > chairs_product_count, "Product count after 'All' filter is not greater than 'Chairs' filter")

if __name__ == "__main__":
    unittest.main()