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
        art_category = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']//a[contains(@href, 'art')]"))
        )
        art_category.click()

        # Wait for the filter sidebar to load
        filter_sidebar = self.wait.until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )

        # Locate the Composition section and find "Matt paper" filter
        composition_label = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(., 'Matt paper')]/span/input"))
        )
        driver.execute_script("arguments[0].click();", composition_label)

        # Wait for filter to apply
        self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-miniature'))
        )

        # Verify number of filtered products is 3
        products_after_filtering = driver.find_elements(By.CLASS_NAME, 'product-miniature')
        self.assertEqual(len(products_after_filtering), 3, "Product count did not match after applying filter.")

        # Locate and click "Clear all" button
        clear_all_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'ok')]"))
        )
        clear_all_button.click()

        # Wait for filter to clear and return to original product count
        self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-miniature'))
        )

        # Verify product count resets to 7
        products_after_clearing = driver.find_elements(By.CLASS_NAME, 'product-miniature')
        self.assertEqual(len(products_after_clearing), 7, "Product count did not reset after clearing filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()