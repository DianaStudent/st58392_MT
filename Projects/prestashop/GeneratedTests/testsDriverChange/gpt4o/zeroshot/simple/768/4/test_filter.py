import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_filter_products(self):
        driver = self.driver

        try:
            # Navigate to "Art" category
            art_category_link = driver.find_element(By.LINK_TEXT, "Art")
            art_category_link.click()

            # Wait for filter sidebar
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters"))
            )

            # Get initial product count
            initial_products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product-miniature")
            initial_count = len(initial_products)

            # Select "Matt paper" filter
            matt_paper_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Matt paper')]"))
            )
            matt_paper_checkbox.click()

            # Wait for product list update
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, "#js-product-list .product-miniature")) < initial_count
            )
            filtered_products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product-miniature")
            filtered_count = len(filtered_products)

            # Ensure product count decreased
            self.assertLess(filtered_count, initial_count, "Product count did not decrease after applying filter")

            # Clear filter
            clear_filters = driver.find_element(By.XPATH, "//a[contains(@class, 'search-link') and contains(., 'Matt paper')]")
            clear_filters.click()

            # Wait for product list update
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, "#js-product-list .product-miniature")) == initial_count
            )
            final_products = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product-miniature")
            final_count = len(final_products)

            # Ensure product count returns to initial
            self.assertEqual(final_count, initial_count, "Product count did not return to initial after clearing filter")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()