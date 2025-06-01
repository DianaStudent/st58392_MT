from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        
        # Navigate to Art category
        art_category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        )
        if not art_category_link:
            self.fail("Art category link not found.")
        art_category_link.click()

        # Wait for the filter sidebar to be present
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )
        if not filter_sidebar:
            self.fail("Filter sidebar not found.")

        # Get initial product count
        initial_products = driver.find_elements(By.CSS_SELECTOR, ".js-product")
        initial_product_count = len(initial_products)
        if initial_product_count == 0:
            self.fail("No products found initially.")

        # Select the "Matt paper" filter
        matt_paper_filter = driver.find_element(By.XPATH, "//a[contains(text(), 'Matt paper')]")
        if not matt_paper_filter:
            self.fail("'Matt paper' filter not found.")
        matt_paper_filter.click()

        # Wait for the page update
        WebDriverWait(driver, 20).until(
            EC.staleness_of(initial_products[0])
        )

        # Verify reduction in the number of visible products
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".js-product")
        filtered_product_count = len(filtered_products)
        if filtered_product_count >= initial_product_count:
            self.fail("Product count did not reduce after applying the filter.")

        # Clear all filters
        clear_all_button = driver.find_element(By.CLASS_NAME, "js-search-toggler")
        if not clear_all_button:
            self.fail("Clear all button not found.")
        clear_all_button.click()

        # Wait for product list to reset
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product"))
        )

        # Verify product count returns to the original count
        final_products = driver.find_elements(By.CSS_SELECTOR, ".js-product")
        final_product_count = len(final_products)
        if final_product_count != initial_product_count:
            self.fail("Product count did not return to initial count after clearing the filter.")

if __name__ == "__main__":
    unittest.main()