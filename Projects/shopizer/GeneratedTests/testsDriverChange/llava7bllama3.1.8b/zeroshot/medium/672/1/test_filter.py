import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_filter_products(self):
        # Click on the "Tables" tab to filter products
        tables_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#filter-medium']/span[text()='Tables']")))
        tables_tab.click()

        # Verify that at least one product appears after filtering by Tables
        filtered_products = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-item")))
        self.assertGreater(len(filtered_products), 0)

        # Click on the "Chairs" tab to change the filter
        chairs_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#filter-medium']/span[text()='Chairs']")))
        chairs_tab.click()

        # Verify that product list is updated after filtering by Chairs
        filtered_products = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-item")))
        self.assertGreater(len(filtered_products), 0)

        # Click "All" to remove the filter
        all_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#filter-medium']/span[text()='All']")))
        all_tab.click()

        # Confirm that full list of products is shown after removing filter
        filtered_products = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-item")))
        self.assertEqual(len(filtered_products), 12)  # This value might need to be updated based on the actual number of products

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()