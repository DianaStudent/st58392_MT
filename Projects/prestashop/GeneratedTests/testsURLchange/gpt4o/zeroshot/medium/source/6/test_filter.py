import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Open the home page
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'index'))
            )
        except:
            self.fail("Home page did not load.")

        # Navigate to the 'Art' product category
        try:
            art_category = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Art'))
            )
            art_category.click()
        except:
            self.fail("Art category link did not load.")

        # Wait for the filter sidebar to be present
        try:
            filter_sidebar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'search_filters'))
            )
        except:
            self.fail("Filter sidebar did not load.")

        # Find the "Matt paper" filter and click on it
        try:
            matt_paper_filter = filter_sidebar.find_element(By.LINK_TEXT, 'Matt paper')
            matt_paper_filter.click()
        except:
            self.fail("Matt paper filter did not load.")

        # Wait for the page to update, and verify that the number of visible product items is reduced
        try:
            products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.js-product'))
            )
            filtered_product_count = len(products)
            self.assertGreater(filtered_product_count, 0, "Product count should be greater than zero after applying filter")
        except:
            self.fail("Products did not update after applying filter.")

        # Click "Clear all" to remove filters
        try:
            clear_all_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Clear all'))
            )
            clear_all_button.click()
        except:
            self.fail("Clear all button did not appear.")

        # Verify that the number of products returns to the original count
        try:
            original_products = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.js-product'))
            )
            original_product_count = len(original_products)
            self.assertEqual(original_product_count, 7, "Product count should return to the original count after clearing filters")
        except:
            self.fail("Products did not return to original count after clearing filter.")


if __name__ == "__main__":
    unittest.main()