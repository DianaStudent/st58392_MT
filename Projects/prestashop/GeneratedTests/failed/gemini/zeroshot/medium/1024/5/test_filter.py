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

        # 3. On the category page, wait for the filter sidebar to be present.
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar not found")

        # Get initial product count
        total_products_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        initial_product_count_text = total_products_element.text
        self.assertIsNotNone(initial_product_count_text)
        self.assertTrue(initial_product_count_text != "")
        initial_product_count = int(initial_product_count_text.split(' ')[1])

        # 4. Select the "Matt paper" filter using label-based selection.
        matt_paper_label = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//section[@class='facet clearfix']//p[contains(text(),'Composition')]/following-sibling::ul//a[contains(text(),'Matt paper')]"))
        )
        matt_paper_label.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='facet-label']/a[contains(@href,'Matt+paper')]"))
        )

        total_products_element_after_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        filtered_product_count_text = total_products_element_after_filter.text
        self.assertIsNotNone(filtered_product_count_text)
        self.assertTrue(filtered_product_count_text != "")

        filtered_product_count = int(filtered_product_count_text.split(' ')[1])
        self.assertLess(filtered_product_count, initial_product_count, "Product count did not decrease after applying filter")

        # 6. Then click the "Clear all" button to remove filters.
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        )
        clear_all_button.click()

        # 7. Verify that the number of products returns to the original count.
        total_products_element_after_clear = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )
        cleared_product_count_text = total_products_element_after_clear.text

        self.assertIsNotNone(cleared_product_count_text)
        self.assertTrue(cleared_product_count_text != "")
        cleared_product_count = int(cleared_product_count_text.split(' ')[1])

        self.assertEqual(cleared_product_count, initial_product_count, "Product count did not return to original count after clearing filters")

if __name__ == "__main__":
    unittest.main()