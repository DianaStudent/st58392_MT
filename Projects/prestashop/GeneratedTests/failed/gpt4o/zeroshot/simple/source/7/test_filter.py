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
    
    def test_filter_product(self):
        driver = self.driver

        # Navigate to the Art category
        art_category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # Wait for the filter sidebar
        try:
            filter_sidebar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters"))
            )
        except:
            self.fail("Filter sidebar not found")

        # Select a checkbox filter by its label text
        try:
            composition_filter = driver.find_element(By.XPATH, "//label[text()=' Matt paper ']/input")
            driver.execute_script("arguments[0].click();", composition_filter)
        except:
            self.fail("Composition filter 'Matt paper' not found")

        # Get initial count of visible products
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature"))

        # Apply filter and wait for product list to update
        WebDriverWait(driver, 20).until(
            lambda d: len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature")) != initial_product_count
        )

        # Get new count of visible products
        filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature"))

        # Verify that the product count has changed
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying filter")

        # Uncheck the filter by its label text to clear filter
        try:
            driver.execute_script("arguments[0].click();", composition_filter)
        except:
            self.fail("Failed to uncheck 'Matt paper' filter")

        # Wait for product list to revert
        WebDriverWait(driver, 20).until(
            lambda d: len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature")) == initial_product_count
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()