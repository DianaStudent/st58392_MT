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

        # Navigate to the 'Art' category page
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Art category: {e}")

        # Wait for the filter sidebar to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar did not load: {e}")

        # Get initial product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
            )
            initial_product_count_text = total_products_element.text
            initial_product_count = int(initial_product_count_text.split(" ")[2])
        except Exception as e:
            self.fail(f"Failed to get initial product count: {e}")

        # Select the 'Matt paper' filter
        try:
            matt_paper_label = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Failed to select 'Matt paper' filter: {e}")

        # Wait for the filter to apply and product list to update
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )

        # Get updated product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
            )
            updated_product_count_text = total_products_element.text
            updated_product_count = int(updated_product_count_text.split(" ")[2])
        except Exception as e:
            self.fail(f"Failed to get updated product count: {e}")

        # Verify that the product count has changed
        self.assertNotEqual(initial_product_count, updated_product_count, "Product count did not change after applying filter.")

        # Clear filter
        try:
            clear_filter_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
            )
            clear_filter_link.click()
        except:
            print("Clear all link not found, assuming no active filters")

        # Wait for the filter to clear and product list to update
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )

        # Get product count after clearing filter
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
            )
            final_product_count_text = total_products_element.text
            final_product_count = int(final_product_count_text.split(" ")[2])
        except Exception as e:
            self.fail(f"Failed to get final product count: {e}")

        # Verify that the product count has returned to the initial count
        self.assertEqual(initial_product_count, final_product_count, "Product count did not return to initial count after clearing filter.")

if __name__ == "__main__":
    unittest.main()