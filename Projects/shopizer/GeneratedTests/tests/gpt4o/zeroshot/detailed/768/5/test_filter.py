import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://localhost/"
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        accept_button = wait.until(EC.presence_of_element_located((By.ID, 'rcc-confirm-button')))
        accept_button.click()

        # Apply "Tables" filter
        tables_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-rb-event-key="tables"]')))
        tables_tab.click()

        # Wait for product grid to update and store the number of products
        tables_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.tab-content .row > div'))
        )
        self.assertTrue(len(tables_products) > 0, "No products displayed for Tables filter.")
        tables_product_count = len(tables_products)

        # Apply "Chairs" filter
        chairs_tab = driver.find_element(By.CSS_SELECTOR, 'a[data-rb-event-key="chairs"]')
        chairs_tab.click()

        # Wait for product grid to update and verify product count change
        chairs_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.tab-content .row > div'))
        )
        self.assertTrue(len(chairs_products) > 0, "No products displayed for Chairs filter.")
        chairs_product_count = len(chairs_products)
        
        self.assertNotEqual(tables_product_count, chairs_product_count, "Product counts for Tables and Chairs filters are the same.")
        
        # Apply "All" filter
        all_tab = driver.find_element(By.CSS_SELECTOR, 'a[data-rb-event-key="all"]')
        all_tab.click()

        # Wait for product grid to update and verify product count increase
        all_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.tab-content .row > div'))
        )
        self.assertTrue(len(all_products) > 0, "No products displayed for All filter.")
        all_product_count = len(all_products)

        self.assertGreater(all_product_count, chairs_product_count, "Product count for All filter is not greater than Chairs filter.")

if __name__ == "__main__":
    unittest.main()