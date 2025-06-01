from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_product_filter(self):
        driver = self.driver

        # Navigate to the "Art" category
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Art']"))
        )
        art_category_link.click()

        # Wait for filter sidebar to be present
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Filter By')]"))
        )

        # Get the initial product count
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature"))

        # Select the filter "Composition" -> "Matt paper"
        composition_filter_label = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Matt paper']"))
        )
        composition_filter_label.click()

        # Wait for the page to update
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature"))
        )

        # Verify that the number of visible product items is reduced
        filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature"))
        self.assertLess(filtered_product_count, initial_product_count, "Product count did not reduce after filter application.")

        # Clear all filters
        clear_filter_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Clear all')]"))
        )
        clear_filter_link.click()

        # Wait for the page to update
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature"))
        )

        # Verify that the number of products returns to the original count
        cleared_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature"))
        self.assertEqual(cleared_product_count, initial_product_count, "Product count did not return to original after clearing filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()