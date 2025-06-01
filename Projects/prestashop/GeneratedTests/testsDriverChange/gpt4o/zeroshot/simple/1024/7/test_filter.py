import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_filter_product_by_composition(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the Art category
        art_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))
        art_link.click()

        # Wait for the filter sidebar to load
        filter_sidebar = wait.until(EC.presence_of_element_located((By.ID, "search_filters")))

        # Find and click the "Matt paper" composition checkbox
        filter_label = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, 'Composition-Matt+paper')]/ancestor::label")))
        filter_label.click()

        # Capture the product count after filter
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature"))

        # Clear the filter by unchecking the checkbox
        filter_label.click()

        # Verify the product count changes after applying and removing the filter
        final_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature"))
        if initial_product_count == final_product_count:
            self.fail("Product count did not change after filtering.")

if __name__ == "__main__":
    unittest.main()