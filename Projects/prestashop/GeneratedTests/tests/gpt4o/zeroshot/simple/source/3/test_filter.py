import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_product_count(self):
        driver = self.driver
        
        # Navigate to Art category
        art_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".category[href*='9-art']")))
        art_link.click()

        # Wait for the filter sidebar
        try:
            filter_sidebar = self.wait.until(EC.visibility_of_element_located((By.ID, "search_filters_wrapper")))
        except:
            self.fail("Filter sidebar did not load.")

        # Find and click "Composition - Matt paper" filter
        try:
            composition_filter_label = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//label[contains(., 'Matt paper')]"
            )))
            composition_filter_label.click()
        except:
            self.fail("Composition filter 'Matt paper' not found.")

        # Verify that the number of product items changes
        try:
            initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))

            # Wait for product list update
            self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))

            filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))
        except:
            self.fail("Product items did not change after applying filter.")

        self.assertNotEqual(initial_product_count, filtered_product_count, 
                            "Product count did not change after applying filter.")

        # Clear the filter
        try:
            clear_filter_element = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#js-active-search-filters .clear-filter"
            )))
            clear_filter_element.click()

            # Wait for product list update
            self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))

            final_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))
        except:
            self.fail("Unable to clear filter or product items did not reset.")

        self.assertEqual(initial_product_count, final_product_count, 
                         "Product count did not reset after clearing filter.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()