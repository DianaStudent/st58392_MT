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
        self.driver.maximize_window()

    def test_filter_product(self):
        driver = self.driver

        # Go to Art category
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Art'))).click()

        # Wait for the filters sidebar to be available
        filters_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'search_filters'))
        )
        if not filters_sidebar:
            self.fail("Filter sidebar not found")

        # Select the "Matt paper" filter
        filter_label = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Matt paper'))
        )
        filter_label.click()

        # Verify that the number of visible product items changes
        products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.js-product'))
        )
        filtered_product_count = len(products)
        self.assertNotEqual(filtered_product_count, 7, "Product count did not change after applying filter")

        # Remove filter
        filter_label.click()

        # Verify the product count reverts back to original
        products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.js-product'))
        )
        restored_product_count = len(products)
        self.assertEqual(restored_product_count, 7, "Product count did not revert back to original after removing filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()