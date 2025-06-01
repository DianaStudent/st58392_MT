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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Art" category in the top menu.
        art_category_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
        )
        art_category_link.click()

        # 3. Wait for the category page to load.
        self.wait.until(
            EC.presence_of_element_located((By.ID, "js-product-list-header"))
        )

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        # Wait for the filter sidebar.
        filter_section = self.wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )

        # Locate the "Composition" section.
        composition_section = filter_section.find_element(
            By.XPATH, ".//section[.//p[contains(text(), 'Composition')]]"
        )

        # Locate the "Matt paper" checkbox within the "Composition" section.
        matt_paper_checkbox_label = composition_section.find_element(
            By.XPATH, ".//label[.//a[contains(text(), 'Matt paper')]]"
        )
        matt_paper_checkbox_input = matt_paper_checkbox_label.find_element(By.XPATH, ".//input[@type='checkbox']")

        # Click the checkbox.
        matt_paper_checkbox_input.click()

        # 5. Do not use dynamic IDs. Use XPath or CSS selectors based on `data-name` and label text. (Done above)

        # 6. Wait for the filter to apply.
        # Wait for the product count to change.
        self.wait.until(lambda driver: self.get_product_count() == 3)

        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        product_count = self.get_product_count()
        self.assertEqual(product_count, 3, "Product count should be 3 after filtering.")

        # 8. Locate and click the "Clear all" button to remove filters.
        # Locate the "Clear all" button.
        # clear_all_button = self.wait.until(
        #     EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        # )
        # clear_all_button.click()

        # 8. Locate and click the "Clear all" button to remove filters.
        # Find the active filters section
        active_filters_section = self.driver.find_element(By.ID, "js-active-search-filters")

        # Find the clear all link within the active filters section
        clear_all_link = active_filters_section.find_element(By.LINK_TEXT, "Clear all")

        # Click the clear all link
        clear_all_link.click()

        # 9. Wait and assert that the number of products returns to the original count - 7.
        # Wait for the product count to revert to 7.
        self.wait.until(lambda driver: self.get_product_count() == 7)

        # Assert that the product count is back to 7.
        product_count_after_clear = self.get_product_count()
        self.assertEqual(product_count_after_clear, 7, "Product count should be 7 after clearing filters.")

    def get_product_count(self):
        try:
            total_products_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            if total_products_element and total_products_element.text:
                text = total_products_element.text
                number = int(text.split(" ")[1])
                return number
            else:
                self.fail("Total products element not found or empty.")
        except Exception as e:
            self.fail(f"Failed to get product count: {e}")

if __name__ == "__main__":
    unittest.main()