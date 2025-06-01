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

        # 1. Open the home page (already done in setUp)

        # 2. Apply the "Tables" filter
        tables_tab_locator = (By.XPATH, "//a[text()='Tables']")
        tables_tab = wait.until(EC.presence_of_element_located(tables_tab_locator))
        tables_tab.click()

        # 3. Wait for product grid to update and check at least one product is visible
        product_locator = (By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        wait.until(EC.presence_of_element_located(product_locator))
        tables_products = driver.find_elements(*product_locator)
        if not tables_products:
            self.fail("No products displayed after applying 'Tables' filter.")
        tables_product_count = len(tables_products)

        # 4. Store number of visible products
        if tables_product_count == 0:
            self.fail("Tables filter returned 0 products")

        # 5. Switch to the "Chairs" filter
        chairs_tab_locator = (By.XPATH, "//a[text()='Chairs']")
        chairs_tab = wait.until(EC.presence_of_element_located(chairs_tab_locator))
        chairs_tab.click()

        # Wait for product grid to update and check at least one product is visible
        wait.until(EC.presence_of_element_located(product_locator))
        chairs_products = driver.find_elements(*product_locator)
        if not chairs_products:
            self.fail("No products displayed after applying 'Chairs' filter.")
        chairs_product_count = len(chairs_products)

        # 6. Verify that the list of products is updated and different from the previous.
        if chairs_product_count == 0:
            self.fail("Chairs filter returned 0 products")

        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count should be different after applying 'Chairs' filter.")

        # 7. Then click the "All" filter to reset
        all_tab_locator = (By.XPATH, "//a[text()='All']")
        all_tab = wait.until(EC.presence_of_element_located(all_tab_locator))
        all_tab.click()

        # Wait for product grid to update and check at least one product is visible
        wait.until(EC.presence_of_element_located(product_locator))
        all_products = driver.find_elements(*product_locator)
        if not all_products:
            self.fail("No products displayed after applying 'All' filter.")
        all_product_count = len(all_products)

        # 8. Confirm that product list contains more items than after previous filters.
        self.assertTrue(all_product_count > tables_product_count and all_product_count > chairs_product_count, "Product count after 'All' filter should be greater than previous filters.")

if __name__ == "__main__":
    unittest.main()