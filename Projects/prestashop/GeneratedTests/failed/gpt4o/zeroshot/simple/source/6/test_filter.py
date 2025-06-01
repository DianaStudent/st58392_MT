from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.driver.maximize_window()

    def test_product_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for the filter sidebar to be present
        try:
            filter_sidebar = wait.until(
                EC.presence_of_element_located((By.ID, "search_filters"))
            )
        except:
            self.fail("Filter sidebar not found")

        # Select the 'Matt paper' filter checkbox
        try:
            matt_paper_label = wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Matt paper')]"))
            )
            matt_paper_label.click()
        except:
            self.fail("Matt paper filter not found")

        # Verify that the number of visible product items changes
        initial_product_count = self.get_visible_product_count()

        # Wait for the product list to update
        wait.until(
            lambda driver: self.get_visible_product_count() != initial_product_count
        )

        new_product_count = self.get_visible_product_count()
        self.assertNotEqual(initial_product_count, new_product_count,
                            "Product count did not change after applying the filter")

        # Remove the filter by clicking it again
        matt_paper_label.click()

        # Verify the product count reverts back
        reverted_product_count = self.get_visible_product_count()
        wait.until(
            lambda driver: reverted_product_count == initial_product_count
        )

    def get_visible_product_count(self):
        driver = self.driver
        products = driver.find_elements(By.CSS_SELECTOR, ".js-product")
        return len([product for product in products if product.is_displayed()])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()