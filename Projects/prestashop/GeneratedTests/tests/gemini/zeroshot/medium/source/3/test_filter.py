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

        # 2. Navigate to a product category.
        art_category_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Art']"))
        )
        if art_category_link:
            art_category_link.click()
        else:
            self.fail("Art category link not found.")

        # 3. On the category page, wait for the filter sidebar to be present.
        filter_sidebar = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        if not filter_sidebar:
            self.fail("Filter sidebar not found.")

        # Get the initial product count
        total_products_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        if total_products_element and total_products_element.text:
            initial_product_count = total_products_element.text
        else:
            self.fail("Initial product count not found or is empty.")

        # 4. Select the filter using label-based selection.
        matt_paper_label = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()=' Matt paper ']"))
        )

        if matt_paper_label:
            matt_paper_label.click()
        else:
            self.fail("Matt paper filter label not found.")

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        wait.until(EC.staleness_of(total_products_element))
        total_products_element_after_filter = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        if total_products_element_after_filter and total_products_element_after_filter.text:
            filtered_product_count = total_products_element_after_filter.text
        else:
            self.fail("Filtered product count not found or is empty.")

        self.assertNotEqual(initial_product_count, filtered_product_count,
                             "Product count did not change after applying the filter.")

        # 6. Then click the "Clear all" button to remove filters.
        # clear_all_button = wait.until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "Clear all"))
        # )

        # if clear_all_button:
        #     clear_all_button.click()
        # else:
        #     self.fail("Clear all button not found.")

        # 7. Verify that the number of products returns to the original count.
        # wait.until(EC.staleness_of(total_products_element_after_filter))
        # total_products_element_after_clear = wait.until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        # )

        # if total_products_element_after_clear and total_products_element_after_clear.text:
        #     cleared_product_count = total_products_element_after_clear.text
        # else:
        #     self.fail("Cleared product count not found or is empty.")

        # self.assertEqual(initial_product_count, cleared_product_count,
        #                  "Product count did not return to the original count after clearing filters.")


if __name__ == "__main__":
    unittest.main()