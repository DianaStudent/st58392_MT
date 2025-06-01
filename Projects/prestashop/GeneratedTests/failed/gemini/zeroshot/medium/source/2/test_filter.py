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
        self.driver.implicitly_wait(10)

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

        # 3. Wait for the filter sidebar to be present.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar did not load: {e}")

        # 4. Select the "Matt paper" filter.
        try:
            matt_paper_label = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()=' Matt paper ']"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Could not click 'Matt paper' filter: {e}")

        # 5. Wait for the page to update and verify that the number of visible product items is reduced.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']"))
            )
            product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list-top']/div[@class='col-lg-5 hidden-sm-down total-products']/p"))
            )

            initial_product_count_text = product_count_element.text
            if not initial_product_count_text:
                self.fail("Initial product count text is empty.")
            initial_product_count = int(initial_product_count_text.split(" ")[2])

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']"))
            )
            product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list-top']/div[@class='col-lg-5 hidden-sm-down total-products']/p"))
            )

            filtered_product_count_text = product_count_element.text
            if not filtered_product_count_text:
                self.fail("Filtered product count text is empty.")
            filtered_product_count = int(filtered_product_count_text.split(" ")[2])

            self.assertLess(filtered_product_count, initial_product_count, "Product count did not decrease after filtering.")

        except Exception as e:
            self.fail(f"Failed to verify product count after filtering: {e}")

        # 6. Click the "Clear all" button to remove filters.
        try:
            clear_all_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Clear all']"))
            )
            clear_all_button.click()
        except Exception as e:
            self.fail(f"Could not click 'Clear all' button: {e}")

        # 7. Verify that the number of products returns to the original count.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']"))
            )
            product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list-top']/div[@class='col-lg-5 hidden-sm-down total-products']/p"))
            )

            after_clear_product_count_text = product_count_element.text
            if not after_clear_product_count_text:
                self.fail("Product count text after clear all is empty.")
            after_clear_product_count = int(after_clear_product_count_text.split(" ")[2])

            self.assertEqual(after_clear_product_count, initial_product_count, "Product count did not return to original after clearing filters.")

        except Exception as e:
            self.fail(f"Failed to verify product count after clearing filters: {e}")

if __name__ == "__main__":
    unittest.main()