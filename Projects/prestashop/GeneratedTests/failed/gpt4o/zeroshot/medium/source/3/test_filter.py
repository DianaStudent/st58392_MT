from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Step 2: Navigate to the 'Art' category
        art_category = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Art')]"))
        )
        art_category.click()

        # Step 3: Wait for filter sidebar on the category page
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='search_filters']"))
        )

        # Validate filter sidebar exists
        if not filter_sidebar:
            self.fail("Filter sidebar is missing")

        # Count initial number of products
        initial_products = len(driver.find_elements(By.CLASS_NAME, 'product-miniature'))

        # Step 4: Select the filter using label-based selection
        composition_filter = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Matt paper')]"))
        )
        composition_filter.click()

        # Step 5: Wait for the page to update and verify product count is reduced
        WebDriverWait(driver, 20).until(
            lambda x: len(x.find_elements(By.CLASS_NAME, 'product-miniature')) < initial_products
        )

        filtered_products = len(driver.find_elements(By.CLASS_NAME, 'product-miniature'))
        self.assertLess(filtered_products, initial_products, "Number of products did not decrease after filtering")

        # Step 6: Click the 'Clear all' link to remove the filter
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary ok']"))
        )
        clear_all_button.click()

        # Step 7: Verify the number of products returns to the original count
        WebDriverWait(driver, 20).until(
            lambda x: len(x.find_elements(By.CLASS_NAME, 'product-miniature')) == initial_products
        )

        final_products = len(driver.find_elements(By.CLASS_NAME, 'product-miniature'))
        self.assertEqual(final_products, initial_products, "Number of products did not return to original count after clearing filter")

if __name__ == '__main__':
    unittest.main()