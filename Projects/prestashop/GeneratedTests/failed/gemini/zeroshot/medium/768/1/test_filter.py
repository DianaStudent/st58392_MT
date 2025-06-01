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

        # 2. Navigate to the "Art" category.
        art_category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # 3. Wait for the filter sidebar to be present.
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar is not present.")

        # Get the initial product count
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )

        if total_products_element and total_products_element.text:
            initial_product_count_text = total_products_element.text
            initial_product_count = int(initial_product_count_text.split(" ")[2])
        else:
            self.fail("Could not retrieve initial product count.")

        # 4. Select the "Matt paper" filter.
        matt_paper_label = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Matt paper"))
        )
        matt_paper_label.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )

        total_products_element_after_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )

        if total_products_element_after_filter and total_products_element_after_filter.text:
            filtered_product_count_text = total_products_element_after_filter.text
            filtered_product_count = int(filtered_product_count_text.split(" ")[2])
        else:
            self.fail("Could not retrieve product count after filtering.")

        self.assertLess(filtered_product_count, initial_product_count,
                         "Product count did not decrease after applying filter.")

        # 6. Clear all filters
        clear_all_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        )
        clear_all_link.click()

        # 7. Verify that the number of products returns to the original count.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )

        total_products_element_after_clear = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )

        if total_products_element_after_clear and total_products_element_after_clear.text:
            final_product_count_text = total_products_element_after_clear.text
            final_product_count = int(final_product_count_text.split(" ")[2])
        else:
            self.fail("Could not retrieve product count after clearing filters.")

        self.assertEqual(initial_product_count, final_product_count,
                         "Product count did not return to original count after clearing filters.")

if __name__ == "__main__":
    unittest.main()