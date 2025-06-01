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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Navigate to the Art category page
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'http://localhost:8080/en/9-art')]"))
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

        # Get the initial product count
        try:
            initial_product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = initial_product_count_element.text
            initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get initial product count: {e}")

        # Select the "Matt paper" filter
        try:
            matt_paper_label = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Failed to select 'Matt paper' filter: {e}")

        # Wait for the page to reload after applying the filter
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
        except Exception as e:
            self.fail(f"Page did not reload after applying filter: {e}")

        # Get the product count after applying the filter
        try:
            filtered_product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            filtered_product_count_text = filtered_product_count_element.text
            filtered_product_count = int("".join(filter(str.isdigit, filtered_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get product count after applying filter: {e}")

        # Verify that the product count has changed
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter.")

        #Clear the filter
        driver.get("http://localhost:8080/en/9-art")

        # Wait for the page to reload after clearing the filter
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
        except Exception as e:
            self.fail(f"Page did not reload after clearing filter: {e}")

        # Get the product count after clearing the filter
        try:
            cleared_product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            cleared_product_count_text = cleared_product_count_element.text
            cleared_product_count = int("".join(filter(str.isdigit, cleared_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get product count after clearing filter: {e}")

        # Verify that the product count has changed back to the initial count
        self.assertEqual(cleared_product_count, initial_product_count, "Product count did not revert to initial count after clearing filter.")

if __name__ == "__main__":
    unittest.main()