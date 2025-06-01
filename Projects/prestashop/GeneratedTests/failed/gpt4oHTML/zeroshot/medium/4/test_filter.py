from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the home page
        # Assert home page loads
        main_header = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        if not main_header:
            self.fail("Home page did not load correctly.")

        # Step 2: Navigate to the 'Art' product category
        art_category_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']")))
        art_category_link.click()

        # Step 3: On the category page, wait for the filter sidebar to be present
        filter_sidebar = wait.until(EC.presence_of_element_located((By.ID, "search_filters")))
        if not filter_sidebar:
            self.fail("Filter sidebar is not present on the category page.")
        
        # Count initial number of products
        product_list = driver.find_elements(By.CSS_SELECTOR, ".js-product")
        initial_product_count = len(product_list)
        
        # Step 4: Select the 'Matt paper' composition filter using label-based selection
        composition_filter_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art?q=Composition-Matt+paper']")))
        composition_filter_label.click()

        # Step 5: Wait for the page to update and verify that the number of visible product items is reduced
        # It's assumed filter changes URL and the page updates
        filtered_product_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product")))
        filtered_product_count = len(filtered_product_list)
        if not filtered_product_list:
            self.fail("No products are visible after applying the filter.")
        self.assertTrue(filtered_product_count < initial_product_count, "Product count did not reduce after applying filter.")
        
        # Step 6: Click the "Clear all" button to remove filters
        # This part is assuming there's a button or link to clear filters, as there isn't a clear "Clear all" in the provided HTML
        # Select a mechanism to clear or navigate back to initial view/parsing URL based on project specifics
        driver.get("http://localhost:8080/en/9-art")  # For the sake of illustration, re-navigate to Art page to clear filters
        
        # Step 7: Verify that the number of products returns to the original count
        product_list_after_clear = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product")))
        product_count_after_clear = len(product_list_after_clear)
        if not product_list_after_clear:
            self.fail("Product list did not repopulate after clearing filters.")
        self.assertEqual(initial_product_count, product_count_after_clear, "Product count did not return to original after clearing filters.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()