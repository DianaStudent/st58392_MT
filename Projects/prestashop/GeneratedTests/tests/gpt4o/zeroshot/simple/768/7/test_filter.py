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
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Navigate to the "Art" category
        art_category_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))
        art_category_link.click()

        # Wait for the filter sidebar to be visible
        self.wait.until(EC.visibility_of_element_located((By.ID, "search_filters")))

        # Check the initial count of products
        initial_products = driver.find_elements(By.CLASS_NAME, "product-miniature")
        initial_count = len(initial_products)

        # Select "Matt paper" filter
        try:
            matt_paper_checkbox = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Matt paper')]/input[@type='checkbox']"))
            )
            matt_paper_checkbox.click()
        except Exception:
            self.fail("Matt paper checkbox is not available.")

        # Verify the product count changes after applying the filter
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "js-product-list"))
        )
        filtered_products = driver.find_elements(By.CLASS_NAME, "product-miniature")
        filtered_count = len(filtered_products)
        self.assertNotEqual(initial_count, filtered_count, "Product count did not change after filtering.")

        # Clear filter by unchecking "Matt paper"
        try:
            matt_paper_checkbox.click()
        except Exception:
            self.fail("Could not uncheck Matt paper checkbox.")

        # Verify the product count returns to initial count after clearing filters
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "js-product-list"))
        )
        final_products = driver.find_elements(By.CLASS_NAME, "product-miniature")
        final_count = len(final_products)
        self.assertEqual(initial_count, final_count, "Product count did not revert back after clearing filters.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()