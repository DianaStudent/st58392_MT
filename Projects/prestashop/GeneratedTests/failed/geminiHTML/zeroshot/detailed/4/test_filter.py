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
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page.
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
        self.wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )

        # Locate the "Composition" filter section.
        composition_section = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//section[.//p[text()='Composition']]"))
        )

        # Locate the "Matt paper" checkbox within the "Composition" section and click it.
        matt_paper_checkbox = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[.//a[text()=' Matt paper ']]/span/input"))
        )
        matt_paper_checkbox.click()

        # 6. Wait for the filter to apply.
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//section[.//p[text()='Composition']]"))
        )

        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        products = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "js-product"))
        )
        initial_product_count = len(products)
        if initial_product_count != 7:
            self.fail(f"Expected 7 products initially, but found {initial_product_count}")

        self.wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 3)
        filtered_products = self.driver.find_elements(By.CLASS_NAME, "js-product")
        filtered_product_count = len(filtered_products)
        self.assertEqual(filtered_product_count, 3,
                         f"Expected 3 products after filtering, but found {filtered_product_count}")

        # 8. Locate and click the "Clear all" button to remove filters.
        # Locate the "Clear all" button
        clear_all_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
        )
        clear_all_button.click()

        # 9. Wait and assert that the number of products returns to the original count - 7.
        self.wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 7)
        products_after_clear = self.driver.find_elements(By.CLASS_NAME, "js-product")
        product_count_after_clear = len(products_after_clear)
        self.assertEqual(product_count_after_clear, 7,
                         f"Expected 7 products after clearing filters, but found {product_count_after_clear}")


if __name__ == "__main__":
    unittest.main()