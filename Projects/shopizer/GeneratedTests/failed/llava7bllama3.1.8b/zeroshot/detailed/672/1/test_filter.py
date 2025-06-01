from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_filtering(self):
        # Apply "Tables" filter
        tables_tab = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Tables')]")))
        tables_tab.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid-item")))

        # Store number of visible products
        initial_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid-item"))))

        # Switch to "Chairs" filter and wait for grid to refresh
        chairs_tab = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Chairs')]")))
        chairs_tab.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid-item")))

        # Verify that the list of products is updated and different from the previous
        updated_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid-item"))))
        self.assertLess(updated_products_count, initial_products_count)

        # Reset to "All" filter
        all_tab = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'All')]")))
        all_tab.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid-item")))

        # Confirm that product list contains more items than after previous filters
        final_products_count = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid-item"))))
        self.assertGreater(final_products_count, updated_products_count)

if __name__ == "__main__":
    unittest.main()