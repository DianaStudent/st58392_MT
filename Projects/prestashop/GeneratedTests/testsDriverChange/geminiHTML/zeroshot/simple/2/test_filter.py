import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # Navigate to Art category page
        try:
            art_category_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Art category: {e}")

        # Wait for the filter sidebar to load
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar did not load: {e}")

        # Get initial product count
        try:
            initial_product_count_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = initial_product_count_element.text
            initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get initial product count: {e}")

        # Apply the "Matt paper" filter
        try:
            matt_paper_label = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art?q=Composition-Matt+paper']"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Failed to apply 'Matt paper' filter: {e}")

        # Wait for the product list to update
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
        except Exception as e:
            self.fail(f"Product list did not update after applying filter: {e}")

        # Get the updated product count
        try:
            updated_product_count_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            updated_product_count_text = updated_product_count_element.text
            updated_product_count = int("".join(filter(str.isdigit, updated_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get updated product count: {e}")

        # Verify that the product count has changed
        self.assertNotEqual(initial_product_count, updated_product_count, "Product count did not change after applying filter.")

        # Clear the filter (navigate back to Art category)
        try:
            art_category_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Art category after filter: {e}")

        # Wait for the product list to update after clearing filter
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
        except Exception as e:
            self.fail(f"Product list did not update after clearing filter: {e}")

        # Get the product count after clearing the filter
        try:
            cleared_product_count_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            cleared_product_count_text = cleared_product_count_element.text
            cleared_product_count = int("".join(filter(str.isdigit, cleared_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get product count after clearing filter: {e}")

        # Verify that the product count has returned to the initial count
        self.assertEqual(initial_product_count, cleared_product_count, "Product count did not return to initial count after clearing filter.")

if __name__ == "__main__":
    unittest.main()