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

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Get initial product count
        products_all = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        initial_product_count = len(products_all)
        self.assertGreater(initial_product_count, 0, "No products displayed initially.")

        # Click on the "Tables" tab
        tables_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']"))
        )
        tables_tab.click()

        # Verify that at least one product appears after filtering
        products_tables = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        tables_product_count = len(products_tables)
        self.assertGreater(tables_product_count, 0, "No tables displayed after filtering.")

        # Click on the "Chairs" tab
        chairs_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']"))
        )
        chairs_tab.click()

        # Verify that product list is updated
        products_chairs = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        chairs_product_count = len(products_chairs)
        self.assertGreater(chairs_product_count, 0, "No chairs displayed after filtering.")
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product count did not change after filtering chairs.")

        # Click "All" to remove the filter
        all_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='All']"))
        )
        all_tab.click()

        # Confirm that the full list of products is shown
        products_all_after = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        all_product_count_after = len(products_all_after)
        self.assertEqual(initial_product_count, all_product_count_after, "Product count after removing filter does not match initial count.")

if __name__ == "__main__":
    unittest.main()