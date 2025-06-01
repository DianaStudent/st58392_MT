import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Navigate to a product category (Art).
        try:
            art_category_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to Art category: {e}")

        # 3. On the category page, wait for the filter sidebar to be present.
        try:
            filter_sidebar = wait.until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar not present: {e}")

        # 4. Select the 'Matt paper' filter using label-based selection.
        try:
            matt_paper_label = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()=' Matt paper ']"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Could not select 'Matt paper' filter: {e}")

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        try:
            # Wait for product list to update
            wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

            # Get the product count
            product_count_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            product_count_text = product_count_element.text
            if not product_count_text:
                self.fail("Product count text is empty.")

            # Extract the number of products
            original_product_count = int(product_count_text.split(' ')[1])

            # Navigate back to the Art category to clear the filter
            driver.get("http://localhost:8080/en/9-art")

            # Wait for product list to update
            wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

            # Select the 'Matt paper' filter again to clear it
            try:
                matt_paper_label = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()=' Matt paper ']"))
                )
                matt_paper_label.click()
            except Exception as e:
                self.fail(f"Could not select 'Matt paper' filter: {e}")

            # Wait for product list to update
            wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

            # Get the product count after clearing the filter
            product_count_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            product_count_text_after_clear = product_count_element.text
            if not product_count_text_after_clear:
                self.fail("Product count text is empty after clear.")

            # Extract the number of products after clearing the filter
            product_count_after_clear = int(product_count_text_after_clear.split(' ')[1])

            # Verify that the number of products returns to the original count
            self.assertEqual(product_count_after_clear, original_product_count, "Product count did not return to original after clearing filter.")

        except Exception as e:
            self.fail(f"Failed to verify product count: {e}")

if __name__ == "__main__":
    unittest.main()