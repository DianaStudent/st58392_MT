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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Wait for and navigate to the "Art" category
        art_category = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']"))
        )
        art_category.click()

        # Wait for the filter sidebar to be present
        filter_sidebar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )
        if not filter_sidebar:
            self.fail("Filter sidebar is not present.")

        # Get original product count
        original_product_count = len(driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product"))

        # Select the "Matt paper" filter
        matt_paper_filter = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Matt paper"))
        )
        matt_paper_filter.click()

        # Wait for the page to update and verify product count is reduced
        WebDriverWait(driver, 20).until(
            EC.staleness_of(driver.find_element(By.CSS_SELECTOR, "#js-product-list .product"))
        )
        filtered_product_count = len(driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product"))

        if filtered_product_count >= original_product_count:
            self.fail("Product count did not reduce after applying filter.")

        # Clear the filter
        clear_filter_button = driver.find_element(By.CSS_SELECTOR, "button.btn-secondary.ok")
        clear_filter_button.click()

        # Verify that the number of products returns to the original count
        WebDriverWait(driver, 20).until(
            EC.staleness_of(driver.find_element(By.CSS_SELECTOR, "#js-product-list .product"))
        )
        reset_product_count = len(driver.find_elements(By.CSS_SELECTOR, "#js-product-list .product"))

        if reset_product_count != original_product_count:
            self.fail("Product count did not return to original after clearing filters.")

if __name__ == "__main__":
    unittest.main()