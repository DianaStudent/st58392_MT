from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8080/en/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the home page.
        self.assertEqual("My Store", driver.title)

        # 2. Navigate to a product category (Art).
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()
        except NoSuchElementException:
            self.fail("Could not find the 'Art' category link.")

        # 3. On the category page, wait for the filter sidebar to be present.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except NoSuchElementException:
            self.fail("Filter sidebar not found.")

        # Get initial product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = total_products_element.text
            if not initial_product_count_text:
                self.fail("Initial product count text is empty.")

            initial_product_count = int(initial_product_count_text.split(' ')[2])
        except NoSuchElementException:
            self.fail("Could not find the total products element.")

        # 4. Select the filter using label-based selection (Composition: Matt paper).
        try:
            composition_filter_label = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Matt paper"))
            )
            composition_filter_label.click()
        except NoSuchElementException:
            self.fail("Could not find the 'Matt paper' filter label.")

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
        except NoSuchElementException:
            self.fail("Could not find the total products element after filtering.")

        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            filtered_product_count_text = total_products_element.text
            if not filtered_product_count_text:
                self.fail("Filtered product count text is empty.")

            filtered_product_count = int(filtered_product_count_text.split(' ')[2])
        except NoSuchElementException:
            self.fail("Could not find the total products element after filtering.")

        self.assertLess(filtered_product_count, initial_product_count,
                         "Product count did not decrease after applying the filter.")

        # 6. Then click the "Clear all" button to remove filters.
        try:
            clear_all_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
            )
            clear_all_button.click()
        except NoSuchElementException:
            self.fail("Could not find the 'Clear all' button.")

        # 7. Verify that the number of products returns to the original count.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
        except NoSuchElementException:
            self.fail("Could not find the total products element after clearing filters.")

        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            after_clear_product_count_text = total_products_element.text
            if not after_clear_product_count_text:
                self.fail("Product count text is empty after clearing filters.")

            after_clear_product_count = int(after_clear_product_count_text.split(' ')[2])
        except NoSuchElementException:
            self.fail("Could not find the total products element after clearing filters.")

        self.assertEqual(initial_product_count, after_clear_product_count,
                         "Product count did not return to the original count after clearing filters.")


if __name__ == "__main__":
    unittest.main()