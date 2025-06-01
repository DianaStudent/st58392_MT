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
        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the "Art" category in the top menu.
        art_category_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]"))
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
        if not filter_section:
            self.fail("Filter section not found.")

        # Select a checkbox filter.
        matt_paper_checkbox = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(text(), 'Matt paper')]/ancestor::label//input[@type='checkbox']")
            )
        )
        matt_paper_checkbox.click()

        # 5. Do not use dynamic IDs. Use XPath or CSS selectors based on `data-name` and label text.
        # Already done

        # 6. Wait for the filter to apply.
        # Wait for filters to take effect by monitoring the number of elements.
        self.wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 3)

        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        product_tiles = self.driver.find_elements(By.CLASS_NAME, "js-product")
        self.assertEqual(len(product_tiles), 3, "Product count is not 3 after applying filter.")

        # 8. Locate and click the "Clear all" button to remove filters.
        # Locate and click the "Clear all" button to remove filters.
        clear_all_button = self.wait.until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "Clear all")
            )
        )
        clear_all_button.click()

        # 9. Wait and assert that the number of products returns to the original count - 7.
        self.wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 7)
        product_tiles_after_clear = self.driver.find_elements(By.CLASS_NAME, "js-product")
        self.assertEqual(len(product_tiles_after_clear), 7, "Product count is not 7 after clearing filter.")


if __name__ == "__main__":
    unittest.main()