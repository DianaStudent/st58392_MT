import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class FilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Use the actual URL as needed
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_filter_products(self):
        driver = self.driver

        # Wait and click on the "Tables" tab
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-rb-event-key, 'tables')]"))
        )
        tables_tab.click()

        # Verify at least one product is displayed
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")))
        products = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")
        if not products:
            self.fail("No products displayed after selecting the 'Tables' filter.")

        initial_table_product_count = len(products)
        self.assertGreater(initial_table_product_count, 0, "No products found in the 'Tables' filter.")

        # Click on the "Chairs" tab
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-rb-event-key, 'chairs')]"))
        )
        chairs_tab.click()

        # Verify product list is updated for "Chairs"
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")))
        products = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")
        if not products:
            self.fail("No products displayed after selecting the 'Chairs' filter.")

        chair_product_count = len(products)
        self.assertNotEqual(initial_table_product_count, chair_product_count, "Product count did not change after applying 'Chairs' filter.")

        # Click on "All" to remove the filter
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-rb-event-key, 'all')]"))
        )
        all_tab.click()

        # Confirm full list of products is shown
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")))
        products = driver.find_elements(By.CSS_SELECTOR, ".tab-content .tab-pane.active.show .product-wrap-2")
        if not products:
            self.fail("No products displayed after selecting the 'All' filter.")

        all_product_count = len(products)
        self.assertNotEqual(chair_product_count, all_product_count, "Product count did not change after removing filter with 'All'.")

if __name__ == "__main__":
    unittest.main()