from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_product_filter_process(self):
        driver = self.driver

        # Step 1: Open the home page
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "index"))
            )
        except:
            self.fail("Home page did not load properly.")

        # Step 2: Navigate to a product category (Art)
        art_category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # Step 3: On the category page, wait for the filter sidebar to be present.
        try:
            filter_sidebar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters"))
            )
        except:
            self.fail("Filter sidebar did not load on the category page.")

        # Count original number of products
        initial_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))

        # Step 4: Select the filter using label-based selection (Composition: Matt paper)
        matt_paper_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Matt paper')]"))
        )
        matt_paper_filter.click()

        # Step 5: Wait for the page to update, and verify that the number of visible product items is reduced.
        WebDriverWait(driver, 20).until(
            lambda d: len(d.find_elements(By.CLASS_NAME, "js-product")) < initial_product_count
        )
        filtered_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))
        self.assertLess(filtered_product_count, initial_product_count)

        # Step 6: Then click the "Clear all" button to remove filters.
        # Waiting for the "Active filters" section to appear
        active_filters = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "js-active-search-filters"))
        )
        clear_filters_button = active_filters.find_element(By.LINK_TEXT, "Clear all")
        clear_filters_button.click()

        # Step 7: Verify that the number of products returns to the original count.
        WebDriverWait(driver, 20).until(
            lambda d: len(d.find_elements(By.CLASS_NAME, "js-product")) == initial_product_count
        )
        final_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))
        self.assertEqual(final_product_count, initial_product_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()