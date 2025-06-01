import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_by_matt_paper_and_clear(self):
        driver = self.driver

        # Click on "Art" category
        try:
            art_category = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']//a[contains(@href, '/9-art')]"))
            )
            art_category.click()
        except Exception:
            self.fail("Failed to navigate to Art category.")

        # Wait for the category page to load
        try:
            filter_sidebar = self.wait.until(
                EC.presence_of_element_located((By.ID, "search_filters"))
            )
        except Exception:
            self.fail("Filter sidebar did not load.")

        # Locate the Composition section and find "Matt paper" filter
        try:
            matt_paper_filter = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(., 'Matt paper')]/span/input"))
            )
            driver.execute_script("arguments[0].click();", matt_paper_filter)
        except Exception:
            self.fail("Failed to find or click on Matt Paper filter.")

        # Wait for the products to be filtered
        try:
            self.wait.until(
                lambda driver: len(driver.find_elements(By.CLASS_NAME, 'product-miniature')) == 3
            )
        except Exception:
            self.fail("Product count did not match after applying filter.")

        # Verify number of filtered products is 3
        products_after_filtering = driver.find_elements(By.CLASS_NAME, 'product-miniature')
        self.assertEqual(len(products_after_filtering), 3, "Product count did not match after applying filter.")

        # Locate and click "Clear all" button
        try:
            clear_all_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Clear all')]"))
            )
            clear_all_button.click()
        except Exception:
            self.fail("Failed to find or click Clear all button.")

        # Wait for the products to reset
        try:
            self.wait.until(
                lambda driver: len(driver.find_elements(By.CLASS_NAME, 'product-miniature')) == 7
            )
        except Exception:
            self.fail("Product count did not reset after clearing filters.")

        # Verify product count resets to 7
        products_after_clearing = driver.find_elements(By.CLASS_NAME, 'product-miniature')
        self.assertEqual(len(products_after_clearing), 7, "Product count did not reset after clearing filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()