from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter_matt_paper(self):
        driver = self.driver
        
        # Step 1: Open the home page and click on "Art" category
        art_category_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
        )
        art_category_link.click()

        # Step 2: Wait for the category page to load and locate the filters
        self.wait.until(
            EC.presence_of_element_located((By.ID, 'search_filters'))
        )

        # Step 3: Apply the "Matt paper" filter under Composition
        matt_paper_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'Composition-Matt+paper')]//preceding-sibling::span//input"))
        )
        matt_paper_checkbox.click()
        
        # Step 4: Wait for the filter to apply and check the number of products
        filtered_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-miniature'))
        )
        
        if not filtered_products or len(filtered_products) != 3:
            self.fail(f"Expected 3 products after applying filter, found {len(filtered_products) if filtered_products else 0}.")

        # Step 5: Clear all filters
        clear_filter_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'facet-label') and contains(text(), 'Composition')]//following-sibling::ul//a[contains(@class, '_gray-darker search-link')][1]"))
        )
        clear_filter_link.click()

        # Step 6: Wait and assert the product count returns to original
        all_products = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-miniature'))
        )
        
        if not all_products or len(all_products) != 7:
            self.fail(f"Expected 7 products after clearing filters, found {len(all_products) if all_products else 0}.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()