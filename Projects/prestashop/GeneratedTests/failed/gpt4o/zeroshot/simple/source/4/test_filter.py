from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to Art category
            art_category_link = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()

            # Wait for the filter sidebar to be present
            wait.until(EC.visibility_of_element_located((By.ID, "search_filters_wrapper")))

            # Initially get the count of visible products
            initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, "#js-product-list .js-product"))

            # Apply the filter by 'Composition' with label 'Matt paper'
            filter_label = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//label[contains(., 'Matt paper')]"))
            )
            filter_label.click()

            # Verify that the number of visible product items changes
            new_product_count = len(wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-product-list .js-product"))
            ))

            self.assertNotEqual(initial_product_count, new_product_count, "Product count did not change after applying filter")

            # Clear the filter by clicking on the filter label again
            filter_label.click()

            # Verify that the number of visible product items reverts
            reverted_product_count = len(wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-product-list .js-product"))
            ))

            self.assertEqual(initial_product_count, reverted_product_count, "Product count did not revert after clearing filter")

        except Exception as e:
            self.fail(f"Test failed due to an unexpected error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()