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
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter_change(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Art category
        art_category_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # Wait for the filter sidebar to be present
        filter_sidebar = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )

        # Capture initial product count
        initial_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        initial_product_count = len(initial_products)

        # Find 'Matt paper' filter checkbox and click it
        matt_paper_checkbox = filter_sidebar.find_element(By.XPATH, "//label[contains(., 'Matt paper')]/span")
        matt_paper_checkbox.click()

        # Wait for the product count to change
        wait.until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, ".product-miniature")) != initial_product_count
        )

        # Capture product count after filter
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        filtered_product_count = len(filtered_products)

        # Check if the product count has changed
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter")

        # Clear the filter to ensure all products are displayed again
        matt_paper_checkbox.click()
        wait.until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, ".product-miniature")) == initial_product_count
        )

        # Capture product count after clearing the filter
        cleared_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        cleared_product_count = len(cleared_products)

        # Verify the product count is back to initial count
        self.assertEqual(initial_product_count, cleared_product_count, "Product count did not reset after clearing filter")

if __name__ == "__main__":
    unittest.main()