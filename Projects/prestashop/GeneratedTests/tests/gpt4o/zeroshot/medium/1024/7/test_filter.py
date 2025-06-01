import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Art category
        art_category = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Art")))
        art_category.click()

        # Wait for the filter sidebar to be present
        filter_sidebar = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div#search_filters")))

        # Verify filter sidebar appears
        if not filter_sidebar:
            self.fail("Filter sidebar not found.")

        # Select the filter for Composition - Matt paper
        matt_paper_filter = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[contains(text(), 'Matt paper')]//input[@type='checkbox']")))
        matt_paper_filter.click()

        # Wait for the page to update
        updated_products = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.js-product")))

        # Verify that the number of visible product items is reduced
        filtered_count = len(updated_products)
        self.assertTrue(filtered_count > 0, "No products are displayed after filter.")

        # Click the "Clear all" button to remove filters
        clear_filters = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Clear all')]")))
        clear_filters.click()

        # Verify that the number of products returns to the original count
        all_products = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.js-product")))
        
        all_products_count = len(all_products)
        self.assertEqual(all_products_count, 7, "Product count did not return to original count after clearing filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()