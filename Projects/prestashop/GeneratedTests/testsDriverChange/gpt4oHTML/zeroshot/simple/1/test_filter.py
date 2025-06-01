import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestArtCategoryFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_by_composition_matt_paper(self):
        driver = self.driver
        wait = self.wait

        try:
            # Wait for the filter sidebar to be present
            wait.until(EC.presence_of_element_located((By.ID, "search_filters_wrapper")))
            
            # Locate the filter sidebar and find the filter for "Composition" with the label "Matt paper"
            composition_section = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='h6 facet-title hidden-sm-down' and contains(text(), 'Composition')]/following-sibling::ul")))
            matt_paper_checkbox_label = composition_section.find_element(By.XPATH, ".//label[contains(., 'Matt paper')]")
            checkbox = matt_paper_checkbox_label.find_element(By.TAG_NAME, "input")

            # Check that checkbox is present
            self.assertIsNotNone(checkbox, "Cannot find the filter checkbox for 'Matt paper'.")

            # Click on the checkbox to apply the filter
            checkbox.click()

            # Verify the number of visible product items changes
            initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div.js-product"))

            # Wait for the products list to update (this may not apply if the test scenario is static without live server)
            wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "div.js-product")) != initial_product_count)

            filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div.js-product"))

            self.assertNotEqual(initial_product_count, filtered_product_count, "The product count did not change after applying the filter.")

            # Remove the filter by unchecking the checkbox
            checkbox.click()

            # Verify the product count returns to initial state
            wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "div.js-product")) == initial_product_count)

            after_clear_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div.js-product"))

            self.assertEqual(initial_product_count, after_clear_product_count, "The product count does not match initial count after clearing the filter.")

        except Exception as e:
            self.fail(f"Test failed due to unexpected exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()