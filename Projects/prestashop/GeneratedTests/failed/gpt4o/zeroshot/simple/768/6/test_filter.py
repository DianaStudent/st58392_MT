from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Navigate to the "Art" category
        art_category_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        )
        art_category_link.click()

        # Wait for the filter sidebar and select "Matt paper" in Composition filter
        filter_sidebar = self.wait.until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )

        composition_filter_label = filter_sidebar.find_element(By.XPATH, "//label[contains(., 'Matt paper')]")
        composition_filter_label.click()

        # Verify that the number of products changes
        initial_product_count = len(driver.find_elements(By.CLASS_NAME, "product-miniature"))
        
        self.wait.until(
            lambda driver: len(driver.find_elements(By.CLASS_NAME, "product-miniature")) != initial_product_count
        )
        filtered_product_count = len(driver.find_elements(By.CLASS_NAME, "product-miniature"))

        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after filtering")

        # Clear the filter by clicking again
        composition_filter_label.click()
        
        # Verify that the number of products returns to the original count
        self.wait.until(
            lambda driver: len(driver.find_elements(By.CLASS_NAME, "product-miniature")) == initial_product_count
        )

        final_product_count = len(driver.find_elements(By.CLASS_NAME, "product-miniature"))
        self.assertEqual(initial_product_count, final_product_count, "Product count did not revert back after clearing filter")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()