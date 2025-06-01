import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Navigate to the Art category page
        try:
            art_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']"))
            )
            art_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to Art category: {e}")

        # Wait for the filter sidebar to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar did not load: {e}")

        # Get the initial product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = total_products_element.text
            initial_product_count = int(initial_product_count_text.split(" ")[1])
        except Exception as e:
            self.fail(f"Could not get initial product count: {e}")

        # Select the "Matt paper" filter
        try:
            matt_paper_label = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()=' Matt paper ']"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Could not select 'Matt paper' filter: {e}")

        # Wait for the filter to be applied and the product list to update
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "js-product-list"))
            )
        except Exception as e:
            self.fail(f"Product list did not update after applying filter: {e}")

        # Get the updated product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            updated_product_count_text = total_products_element.text
            updated_product_count = int(updated_product_count_text.split(" ")[1])
        except Exception as e:
            self.fail(f"Could not get updated product count: {e}")

        # Verify that the product count has changed
        self.assertNotEqual(initial_product_count, updated_product_count, "Product count did not change after applying filter.")

        # Clear the filter
        try:
            clear_filter_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Clear all']"))
            )
            clear_filter_link.click()
        except Exception as e:
            self.fail(f"Could not clear the filter: {e}")

        # Wait for the filter to be cleared and the product list to update
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "js-product-list"))
            )
        except Exception as e:
            self.fail(f"Product list did not update after clearing filter: {e}")

        # Get the product count after clearing the filter
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            final_product_count_text = total_products_element.text
            final_product_count = int(final_product_count_text.split(" ")[1])
        except Exception as e:
            self.fail(f"Could not get final product count: {e}")

        # Verify that the product count has changed back to the initial count
        self.assertEqual(initial_product_count, final_product_count, "Product count did not change back to initial count after clearing filter.")

if __name__ == "__main__":
    unittest.main()