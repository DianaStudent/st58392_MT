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

        # 2. Navigate to a product category ("Art").
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # 3. On the category page, wait for the filter sidebar to be present.
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar is not present.")

        # Get the initial product count
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        initial_product_count_text = total_products_element.text
        if not initial_product_count_text:
            self.fail("Initial product count text is empty.")
        initial_product_count = int(initial_product_count_text.split(' ')[1])

        # 4. Select the filter using label-based selection ("Matt paper").
        filter_label_text = "Matt paper"
        filter_label_locator = (By.XPATH, f'//section[@class="facet clearfix"]//p[contains(text(), "Composition")]/following-sibling::ul//label[contains(., "{filter_label_text}")]/span/input')
        filter_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(filter_label_locator)
        )
        filter_checkbox.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        WebDriverWait(driver, 20).until(
            EC.staleness_of(total_products_element)
        )
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        filtered_product_count_text = total_products_element.text
        if not filtered_product_count_text:
            self.fail("Filtered product count text is empty.")
        filtered_product_count = int(filtered_product_count_text.split(' ')[1])

        self.assertLess(filtered_product_count, initial_product_count, "Product count did not decrease after filtering.")

        # 6. Then click the "Clear all" button to remove filters.
        clear_all_button_locator = (By.LINK_TEXT, "Clear all")
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(clear_all_button_locator)
        )
        clear_all_button.click()

        # 7. Verify that the number of products returns to the original count.
        WebDriverWait(driver, 20).until(
            EC.staleness_of(total_products_element)
        )
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        after_clear_product_count_text = total_products_element.text
        if not after_clear_product_count_text:
            self.fail("Product count text after clear filter is empty.")
        after_clear_product_count = int(after_clear_product_count_text.split(' ')[1])

        self.assertEqual(initial_product_count, after_clear_product_count, "Product count did not return to the original count after clearing filters.")

if __name__ == "__main__":
    unittest.main()