from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_process(self):
        driver = self.driver
        wait = self.wait
        
        # Open product category "Art"
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # Wait for filter sidebar to be present
        filter_sidebar_present = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )
        if not filter_sidebar_present:
            self.fail("Filter sidebar is not present")

        # Select the filter by label-based selection "Composition Matt paper"
        matt_paper_filter = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'Composition-Matt+paper')]"))
        )
        matt_paper_filter.click()

        # Verify the number of products is reduced
        filtered_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature"))
        )
        filtered_count = len(filtered_products)
        if filtered_count == 0:
            self.fail("No products found after applying filter")
        
        self.assertLess(filtered_count, 7, "Filter did not reduce the number of products")

        # Clear all filters
        clear_filters_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//section[@id='js-active-search-filters']/following-sibling::section"))
        )
        clear_filters_button.click()

        # Verify the number of products returns to original count
        all_products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature"))
        )
        all_count = len(all_products)
        
        self.assertEqual(all_count, 7, "Product count did not return to original after clearing filters")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()