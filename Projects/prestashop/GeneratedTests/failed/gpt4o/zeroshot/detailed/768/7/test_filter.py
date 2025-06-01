from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to "Art" category
        art_category_selector = (By.XPATH, "//a[text()=' Art ']")
        wait.until(EC.element_to_be_clickable(art_category_selector)).click()

        # Wait for category page to load
        products_list_selector = (By.ID, "js-product-list")
        wait.until(EC.presence_of_element_located(products_list_selector))

        # Verify initial product count
        initial_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        self.assertEqual(len(initial_products), 7, "Initial product count is not 7")

        # Apply "Matt paper" filter under "Composition"
        matt_paper_filter_selector = (By.XPATH, "//label[contains(text(),'Matt paper')]")
        wait.until(EC.element_to_be_clickable(matt_paper_filter_selector)).click()

        # Wait for filter to apply (product count reduces)
        def product_count_is_reduced(driver):
            return len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature")) == 3

        wait.until(product_count_is_reduced)

        # Verify product count after filtering
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        self.assertEqual(len(filtered_products), 3, "Filtered product count is not 3")

        # Clear all filters
        clear_filters_selector = (By.XPATH, "//button[contains(text(),'Clear all')]")
        wait.until(EC.element_to_be_clickable(clear_filters_selector)).click()

        # Wait for filters to clear (product count returns to original)
        def product_count_is_reset(driver):
            return len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature")) == 7

        wait.until(product_count_is_reset)

        # Verify product count after clearing filters
        final_products = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        self.assertEqual(len(final_products), 7, "Product count after clearing filters is not 7")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()