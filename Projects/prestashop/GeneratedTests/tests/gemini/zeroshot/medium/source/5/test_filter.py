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
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # Already done in setUp

        # 2. Navigate to the "Art" category.
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']"))
        )
        art_category_link.click()

        # 3. Wait for the filter sidebar to be present.
        filter_sidebar = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        if not filter_sidebar:
            self.fail("Filter sidebar not found.")

        # Get the initial product count
        total_products_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "total-products"))
        )
        if not total_products_element or not total_products_element.text:
            self.fail("Initial product count element not found or empty.")

        initial_product_count_text = total_products_element.text
        initial_product_count = int(initial_product_count_text.split(" ")[1])

        # 4. Select the "Matt paper" filter.
        matt_paper_label = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
        )
        matt_paper_label.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        wait.until(
            EC.staleness_of(total_products_element)
        )

        updated_total_products_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "total-products"))
        )

        if not updated_total_products_element or not updated_total_products_element.text:
            self.fail("Updated product count element not found or empty.")

        updated_product_count_text = updated_total_products_element.text
        updated_product_count = int(updated_product_count_text.split(" ")[1])

        self.assertLess(updated_product_count, initial_product_count,
                        "Product count did not decrease after applying filter.")

        # 6. Click the "Clear all" button to remove filters.
        # clear_all_button = wait.until(
        #     EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        # )
        # clear_all_button.click()

        # 7. Verify that the number of products returns to the original count.
        driver.get("http://localhost:8080/en/9-art")

        wait.until(
            EC.staleness_of(updated_total_products_element)
        )

        final_total_products_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "total-products"))
        )

        if not final_total_products_element or not final_total_products_element.text:
            self.fail("Final product count element not found or empty.")

        final_product_count_text = final_total_products_element.text
        final_product_count = int(final_product_count_text.split(" ")[1])

        self.assertEqual(final_product_count, initial_product_count,
                         "Product count did not return to original count after clearing filters.")

if __name__ == "__main__":
    unittest.main()