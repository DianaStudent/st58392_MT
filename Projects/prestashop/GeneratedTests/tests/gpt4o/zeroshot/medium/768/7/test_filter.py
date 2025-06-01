import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Navigate to the Art category
        art_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        art_category.click()

        # Step 3: Wait for filter sidebar to be present
        filter_sidebar = wait.until(EC.presence_of_element_located((By.ID, "search_filters_wrapper")))

        # Check if filter sidebar is visible
        if not filter_sidebar:
            self.fail("Filter sidebar not found")

        # Step 4: Select the 'Matt paper' filter
        matt_paper_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'Composition-Matt+paper')]")))
        matt_paper_filter.click()

        # Step 5: Wait for page to update and verify product items are reduced
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        self.assertLess(len(filtered_products), 7, "Product count did not decrease after applying filter")

        # Step 6: Click 'Clear all' to remove filters
        clear_filter = driver.find_element(By.CSS_SELECTOR, ".search-filters-clear-all > a")
        clear_filter.click()

        # Step 7: Verify the original product count is restored
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
        all_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        self.assertEqual(len(all_products), 7, "Product count did not return to original count after clearing filter")

if __name__ == "__main__":
    unittest.main()