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
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # Already done in setUp

        # 2. Navigate to a product category (Art).
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']"))
        )
        art_category_link.click()

        # 3. On the category page, wait for the filter sidebar to be present.
        filter_sidebar = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        if not filter_sidebar:
            self.fail("Filter sidebar not found.")

        # Get initial product count
        total_products_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        if total_products_element and total_products_element.text:
            initial_product_count_text = total_products_element.text
            initial_product_count = int(initial_product_count_text.split(' ')[2])
        else:
            self.fail("Could not retrieve initial product count.")

        # 4. Select the filter using label-based selection (Composition - Matt paper).
        matt_paper_label = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()=' Matt paper ']"))
        )
        matt_paper_label.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        wait.until(EC.staleness_of(total_products_element))
        updated_total_products_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        if updated_total_products_element and updated_total_products_element.text:
            updated_product_count_text = updated_total_products_element.text
            updated_product_count = int(updated_product_count_text.split(' ')[2])
        else:
            self.fail("Could not retrieve updated product count.")

        self.assertLess(updated_product_count, initial_product_count,
                        "Product count did not decrease after applying filter.")

        # 6. Then click the "Clear all" button to remove filters.
        clear_all_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        )
        clear_all_button.click()

        # 7. Verify that the number of products returns to the original count.
        wait.until(EC.staleness_of(updated_total_products_element))
        final_total_products_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        if final_total_products_element and final_total_products_element.text:
            final_product_count_text = final_total_products_element.text
            final_product_count = int(final_product_count_text.split(' ')[2])
        else:
            self.fail("Could not retrieve final product count.")

        self.assertEqual(final_product_count, initial_product_count,
                         "Product count did not return to original count after clearing filters.")

if __name__ == "__main__":
    unittest.main()