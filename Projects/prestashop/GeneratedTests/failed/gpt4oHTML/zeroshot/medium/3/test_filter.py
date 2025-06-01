from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_products(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the home page
        driver.get("http://localhost:8080/en/")
        
        # 2. Navigate to a product category
        try:
            category_link = driver.find_element(By.LINK_TEXT, "Art")
        except:
            self.fail("Category link 'Art' not found")
        category_link.click()

        # 3. On the category page, wait for the filter sidebar to be present
        try:
            filter_sidebar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search_filters")))
        except:
            self.fail("Filter sidebar was not loaded in time")

        # 4. Select the filter using label-based selection
        try:
            in_stock_filter = driver.find_element(By.LINK_TEXT, "Matt paper")
        except:
            self.fail("Filter 'Matt paper' not found")
        in_stock_filter.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced
        try:
            products_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-product-list .js-product")))
            initial_count = len(products_list)
            new_count = len(driver.find_elements(By.CSS_SELECTOR, "#js-product-list .js-product"))
        except:
            self.fail("Product list elements were not found after filter applied")

        self.assertNotEqual(initial_count, new_count, "Product count did not change after applying filter")

        # 6. Then click the "Clear all" button to remove filters
        try:
            clear_all_button = driver.find_element(By.CSS_SELECTOR, "#js-active-search-filters button")
        except:
            self.fail("Clear all button not found")
        clear_all_button.click()

        # 7. Verify that the number of products returns to the original count
        try:
            products_after_clear = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-product-list .js-product")))
            final_count = len(products_after_clear)
        except:
            self.fail("Product list elements were not found after clearing filters")

        self.assertEqual(initial_count, final_count, "Product count did not return to initial after clearing filters")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()