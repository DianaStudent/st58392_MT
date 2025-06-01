from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFiltering(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode for testing
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.base_url = "http://localhost:8080/en/9-art"

    def test_filter_product_by_composition(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Wait for the filter sidebar to be visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_filters_wrapper"))
        )

        # Locate the 'Composition' filter and select 'Matt paper'
        try:
            composition_section = driver.find_element(By.XPATH, "//section[contains(., 'Composition')]")
            composition_section.click()  # Expand the section if needed

            matt_paper_checkbox = driver.find_element(By.XPATH, "//label[contains(., 'Matt paper')]")
            matt_paper_checkbox.click()

            # Wait for the product list to update
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-product-list .js-product"))
            )

            # Get the number of products and verify the count
            products_before_clear = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .js-product")
            if len(products_before_clear) == 0:
                self.fail("No products were visible after applying the filter.")

            # Now clear the filter by clicking the same checkbox again
            matt_paper_checkbox = driver.find_element(By.XPATH, "//label[contains(., 'Matt paper')]")
            matt_paper_checkbox.click()

            # Wait for the product list to update again
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-product-list .js-product"))
            )

            products_after_clear = driver.find_elements(By.CSS_SELECTOR, "#js-product-list .js-product")
            self.assertNotEqual(len(products_before_clear), len(products_after_clear),
                                "Product count did not change after filtering and clearing.")

        except Exception as e:
            self.fail(f"Test failed due to unexpected error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()