import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_filtering(self):
        # Wait for the filter sidebar
        wait = WebDriverWait(self.driver, 20)
        sidebar_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#filter-sidebar")))
        
        # Select a checkbox filter by its label text
        filter_checkbox_label_text = "Price: €1-€50"
        filter_checkbox = self.driver.find_element_by_css_selector("label[title='{}']".format(filter_checkbox_label_text))
        filter_checkbox.click()
        
        # Wait for the product list to update
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-item")))
        
        # Verify that the number of visible product items changes
        initial_product_count = len(self.driver.find_elements_by_css_selector("div.product-item"))
        time.sleep(1)  # let the products load
        filtered_product_count = len(self.driver.find_elements_by_css_selector("div.product-item"))
        self.assertGreater(filtered_product_count, initial_product_count)
        
        # Remove the filter and verify that the product count changes back
        filter_checkbox.click()
        time.sleep(1)  # let the products load
        removed_filtered_product_count = len(self.driver.find_elements_by_css_selector("div.product-item"))
        self.assertEqual(removed_filtered_product_count, initial_product_count)

if __name__ == "__main__":
    unittest.main()