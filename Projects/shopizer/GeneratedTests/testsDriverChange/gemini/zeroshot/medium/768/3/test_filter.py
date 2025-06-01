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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def get_product_count(self):
        """Counts the number of product elements displayed."""
        product_elements = self.driver.find_elements(By.XPATH, "//div[@class='product-wrap-2 mb-25']")
        return len(product_elements)

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # Accept cookies if present
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Get initial product count
        initial_product_count = self.get_product_count()
        if initial_product_count == 0:
            self.fail("Initial product count is 0. No products displayed on the homepage.")

        # 2. Click on the "Tables" tab to filter products.
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # 3. Verify that at least one product appears.
        tables_product_count = self.get_product_count()
        if tables_product_count == 0:
            self.fail("No tables are displayed after filtering.")

        # 4. Click on the "Chairs" tab to change the filter.
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # 5. Verify that product list is updated.
        chairs_product_count = self.get_product_count()
        if chairs_product_count == 0:
            self.fail("No chairs are displayed after filtering.")

        # Verify that product count is updated
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product list is not updated after filtering.")

        # 6. Click "All" to remove the filter.
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # 7. Confirm that the full list of products is shown.
        all_product_count = self.get_product_count()
        self.assertEqual(initial_product_count, all_product_count, "Product list is not updated after removing filter.")


if __name__ == "__main__":
    unittest.main()