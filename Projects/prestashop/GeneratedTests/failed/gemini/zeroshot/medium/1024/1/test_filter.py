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
        # 1. Open the home page.
        # 2. Navigate to a product category.
        art_category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # 3. On the category page, wait for the filter sidebar to be present.
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar is not present")

        # Get the initial product count
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        initial_product_count_text = total_products_element.text
        self.assertIsNotNone(initial_product_count_text, "Initial product count text is None")
        self.assertTrue(initial_product_count_text != "", "Initial product count is empty")
        initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))

        # 4. Select the filter using label-based selection.
        composition_filter_label = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Matt paper"))
        )
        composition_filter_label.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        )

        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        filtered_product_count_text = total_products_element.text
        self.assertIsNotNone(filtered_product_count_text, "Filtered product count text is None")
        self.assertTrue(filtered_product_count_text != "", "Filtered product count is empty")
        filtered_product_count = int("".join(filter(str.isdigit, filtered_product_count_text)))

        self.assertLess(filtered_product_count, initial_product_count,
                        "Product count did not decrease after applying filter")

        # 6. Then click the "Clear all" button to remove filters.
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        )
        clear_all_button.click()

        # 7. Verify that the number of products returns to the original count.
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        after_clear_product_count_text = total_products_element.text
        self.assertIsNotNone(after_clear_product_count_text, "Product count text after clear is None")
        self.assertTrue(after_clear_product_count_text != "", "Product count after clear is empty")
        after_clear_product_count = int("".join(filter(str.isdigit, after_clear_product_count_text)))

        self.assertEqual(after_clear_product_count, initial_product_count,
                         "Product count did not return to original after clearing filters")

if __name__ == "__main__":
    unittest.main()