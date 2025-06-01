from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Navigate to the "Art" product category.
        try:
            art_category_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            art_category_link.click()
        except (NoSuchElementException, TimeoutException):
            self.fail("Could not find or click the 'Art' category link.")

        # 3. On the category page, wait for the filter sidebar to be present.
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except TimeoutException:
            self.fail("Filter sidebar did not load.")

        # 4. Select the "Matt paper" filter.
        try:
            matt_paper_label = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
            )
            matt_paper_label.click()
        except (NoSuchElementException, TimeoutException):
            self.fail("Could not find or click the 'Matt paper' filter.")

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        try:
            initial_product_count_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = initial_product_count_element.text
            if not initial_product_count_text:
                self.fail("Initial product count text is empty.")
            initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))

            self.wait.until(
                EC.staleness_of(initial_product_count_element)
            )

            filtered_product_count_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            filtered_product_count_text = filtered_product_count_element.text
            if not filtered_product_count_text:
                self.fail("Filtered product count text is empty.")
            filtered_product_count = int("".join(filter(str.isdigit, filtered_product_count_text)))

            self.assertLess(filtered_product_count, initial_product_count,
                            "Product count did not decrease after applying the filter.")

        except (NoSuchElementException, TimeoutException, ValueError) as e:
            self.fail(f"Failed to verify product count after filtering: {e}")

        # 6. Then click the "Clear all" button to remove filters.
        try:
            clear_all_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
            )
            clear_all_button.click()
        except (NoSuchElementException, TimeoutException):
            print("Clear all button not found, trying alternative method")
            try:
                clear_all_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Clear all')]"))
                )
                clear_all_button.click()
            except:
                self.fail("Could not find or click the 'Clear all' button.")

        # 7. Verify that the number of products returns to the original count.
        try:
            self.wait.until(
                EC.staleness_of(filtered_product_count_element)
            )

            final_product_count_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            final_product_count_text = final_product_count_element.text
            if not final_product_count_text:
                self.fail("Final product count text is empty.")
            final_product_count = int("".join(filter(str.isdigit, final_product_count_text)))

            self.assertEqual(final_product_count, initial_product_count,
                             "Product count did not return to the original count after clearing filters.")

        except (NoSuchElementException, TimeoutException, ValueError) as e:
            self.fail(f"Failed to verify product count after clearing filters: {e}")

if __name__ == "__main__":
    unittest.main()