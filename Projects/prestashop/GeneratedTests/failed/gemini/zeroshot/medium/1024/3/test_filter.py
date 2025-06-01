from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        # 1. Open the home page. (Done in setUp)

        # 2. Navigate to the "Art" category.
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to Art category: {e}")

        # 3. On the category page, wait for the filter sidebar to be present.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar not present: {e}")

        # Get the initial product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
            )
            initial_product_count_text = total_products_element.text
            self.assertIsNotNone(initial_product_count_text, "Initial product count text is None")
            self.assertTrue(initial_product_count_text.strip() != "", "Initial product count text is empty")
            initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))
        except Exception as e:
            self.fail(f"Could not get initial product count: {e}")

        # 4. Select the "Matt paper" filter.
        try:
            matt_paper_label = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()=' Matt paper ']"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Could not select 'Matt paper' filter: {e}")

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
            )
            total_products_element = driver.find_element(By.CSS_SELECTOR, ".total-products p")
            filtered_product_count_text = total_products_element.text
            self.assertIsNotNone(filtered_product_count_text, "Filtered product count text is None")
            self.assertTrue(filtered_product_count_text.strip() != "", "Filtered product count text is empty")
            filtered_product_count = int("".join(filter(str.isdigit, filtered_product_count_text)))
            self.assertLess(filtered_product_count, initial_product_count,
                            "Product count did not decrease after filtering")
        except Exception as e:
            self.fail(f"Could not verify product count after filtering: {e}")

        # 6. Then click the "Clear all" button to remove filters.
        try:
            clear_all_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
            )
            clear_all_button.click()
        except Exception as e:
            self.fail(f"Could not click 'Clear all' button: {e}")

        # 7. Verify that the number of products returns to the original count.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
            )
            total_products_element = driver.find_element(By.CSS_SELECTOR, ".total-products p")
            after_clear_product_count_text = total_products_element.text
            self.assertIsNotNone(after_clear_product_count_text, "After clear product count text is None")
            self.assertTrue(after_clear_product_count_text.strip() != "", "After clear product count text is empty")
            after_clear_product_count = int("".join(filter(str.isdigit, after_clear_product_count_text)))
            self.assertEqual(after_clear_product_count, initial_product_count,
                             "Product count did not return to original after clearing filters")
        except Exception as e:
            self.fail(f"Could not verify product count after clearing filters: {e}")

if __name__ == "__main__":
    unittest.main()