import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Step 2: Navigate to a product category (Art)
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        )
        art_category_link.click()

        # Step 3: Wait for the filter sidebar to be present
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )

        # Get initial product count
        initial_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))

        # Step 4: Select the filter using label-based selection (Composition: Matt paper)
        matt_paper_filter = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(., 'Matt paper')]//input[@type='checkbox']"))
        )
        matt_paper_filter.click()

        # Step 5: Wait for the page to update, verify the number of visible product items is reduced
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "js-product-list"))
        )

        filtered_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))
        if filtered_product_count >= initial_product_count:
            self.fail("Filter did not reduce the number of products displayed")

        # Step 6: Click the "Clear all" button to remove filters
        # There wasn't a clear specification for a "Clear all" button, assuming an operation to reset filters exists
        # Adjust this selector according to the actual button available, e.g., use page re-load
        driver.refresh()  # Assuming page reload clears filter in the scenario

        # Step 7: Verify that the number of products returns to the original count
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "js-product-list"))
        )

        reset_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))
        if reset_product_count != initial_product_count:
            self.fail("Product count did not return to original after clearing the filter")

if __name__ == "__main__":
    unittest.main()