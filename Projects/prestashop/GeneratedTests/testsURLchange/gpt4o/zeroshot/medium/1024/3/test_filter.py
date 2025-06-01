import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_product_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Navigate to the Art category page
        category_art = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
        )
        if not category_art:
            self.fail("Art category link not found or not visible.")

        category_art.click()

        # Step 3: Wait for the filter sidebar
        search_filters = wait.until(
            EC.visibility_of_element_located((By.ID, "search_filters"))
        )
        if not search_filters:
            self.fail("Filter sidebar not found or not visible.")

        # Step 4: Select the "Matt paper" filter
        filter_composition = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
        )
        if not filter_composition:
            self.fail("Matt paper filter not found or not visible.")

        filter_composition.click()

        # Step 5: Wait for page update and product count reduction
        products_list = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .product"))
        )
        if not products_list or len(products_list) == 0:
            self.fail("No products found after applying filter.")

        initial_product_count = len(products_list)
        if initial_product_count >= 7:
            self.fail("Product count did not reduce after applying filter.")

        # Step 6: Click "Clear all" - assuming such functionality exists in the system
        clear_filter = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[id='js-active-search-filters'] .btn"))
        )
        if not clear_filter:
            self.fail("Clear all filter button not found or not visible.")

        clear_filter.click()

        # Step 7: Verify the number of products returns to the original count
        products_list_after_clear = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .product"))
        )
        if not products_list_after_clear or len(products_list_after_clear) == 0:
            self.fail("No products found after clearing filter.")

        final_product_count = len(products_list_after_clear)
        if final_product_count != 7:
            self.fail("Product count did not return to original after clearing filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()