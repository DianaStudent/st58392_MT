import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.url = "http://localhost:8080/en/"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Navigate to the "Art" category
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]"))
        )
        art_category_link.click()

        # 2. Wait for the filter sidebar to be present
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        self.assertIsNotNone(filter_sidebar, "Filter sidebar is not present")

        # 3. Get initial product count
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        self.assertIsNotNone(total_products_element, "Total products element is not present")
        initial_product_count_text = total_products_element.text
        self.assertTrue(initial_product_count_text, "Initial product count text is empty")
        initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))

        # 4. Select "Matt paper" filter
        matt_paper_label = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
        )
        self.assertIsNotNone(matt_paper_label, "Matt paper label is not present")
        matt_paper_label.click()

        # 5. Wait for the page to update and get the new product count
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'facet-label')]//a[contains(text(), 'Matt paper')]"))
        )
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        self.assertIsNotNone(total_products_element, "Total products element is not present")
        filtered_product_count_text = total_products_element.text
        self.assertTrue(filtered_product_count_text, "Filtered product count text is empty")
        filtered_product_count = int("".join(filter(str.isdigit, filtered_product_count_text)))

        # 6. Verify that the product count is reduced
        self.assertLess(filtered_product_count, initial_product_count, "Product count was not reduced after filtering")

        # 7. Clear all filters
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Clear all"))
        )
        self.assertIsNotNone(clear_all_button, "Clear all button is not present")
        clear_all_button.click()

        # 8. Wait for the page to update and get the product count after clearing filters
        WebDriverWait(driver, 20).until(
            EC.staleness_of(total_products_element)
        )
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        self.assertIsNotNone(total_products_element, "Total products element is not present")
        after_clear_product_count_text = total_products_element.text
        self.assertTrue(after_clear_product_count_text, "Product count text after clear filter is empty")
        after_clear_product_count = int("".join(filter(str.isdigit, after_clear_product_count_text)))

        # 9. Verify that the product count returns to the original count
        self.assertEqual(after_clear_product_count, initial_product_count, "Product count did not return to original count after clearing filters")

if __name__ == "__main__":
    unittest.main()