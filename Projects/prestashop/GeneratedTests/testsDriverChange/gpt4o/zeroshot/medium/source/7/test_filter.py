import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_product_filter(self):
        driver = self.driver

        # Step 1: Navigate to the "Art" category
        art_category = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Art")))
        art_category.click()

        # Step 2: Wait for the filter sidebar to be present
        filter_sidebar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "search_filters")))

        if not filter_sidebar:
            self.fail("Filter sidebar not found.")

        # Step 3: Select the "Matt paper" filter
        composition_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Matt paper')]"))
        )
        composition_filter.click()

        # Step 4: Wait for the page to update and verify product count reduced
        product_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "js-product-list")))
        
        filtered_products = product_list.find_elements(By.CLASS_NAME, "product-miniature")
        self.assertTrue(filtered_products, "No products found after applying filter.")
        original_count = len(filtered_products)
        
        if original_count >= 7:
            self.fail("Product count did not reduce after applying filter.")

        # Step 5: Click the "Clear all" button to remove filters
        clear_filters_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Clear all')]"))
        )
        clear_filters_button.click()

        # Step 6: Verify product count returns to the original count
        product_list_after_clear = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "js-product-list")))
        cleared_products = product_list_after_clear.find_elements(By.CLASS_NAME, "product-miniature")
        
        if not cleared_products:
            self.fail("Products not found after clearing filter.")

        cleared_count = len(cleared_products)
        if cleared_count != 7:
            self.fail("Product count did not return to original after clearing filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()