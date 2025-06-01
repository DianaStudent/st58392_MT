import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/")

    def test_filter_product(self):
        driver = self.driver

        # Navigate to Art category
        art_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Art')))
        if not art_link:
            self.fail("Art category link not found.")
        art_link.click()

        # Wait for filter sidebar
        filter_sidebar = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#search_filters'))
        )
        if not filter_sidebar:
            self.fail("Filter sidebar not present.")

        # Select the 'Matt paper' filter
        matt_paper_filter = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Matt paper'))
        )
        if not matt_paper_filter:
            self.fail("Matt paper filter not found.")
        matt_paper_filter.click()

        # Wait for the product list to update
        filtered_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-miniature'))
        )

        # Verify the number of visible product items is reduced
        if not filtered_products or len(filtered_products) == 0:
            self.fail("Filtered products not updated correctly.")
        filtered_count = len(filtered_products)
        self.assertLess(filtered_count, 7, "Product count not reduced after filtering.")

        # Click the "Clear all" button to remove filters
        clear_all_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Clear all'))
        )
        if not clear_all_button:
            self.fail("Clear all button not found.")
        clear_all_button.click()

        # Verify that the number of products returns to the original count
        all_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-miniature'))
        )

        if not all_products or len(all_products) == 0:
            self.fail("Products not reset after clearing filters.")
        all_count = len(all_products)
        self.assertEqual(all_count, 7, "Product count did not return to original after clearing filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()