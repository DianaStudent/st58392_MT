import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCategoryFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://example.com/category-a")  # Replace with actual URL for testing
        self.driver.maximize_window()

    def test_filter_brand_and_price(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Apply the "Brand A" checkbox filter
        try:
            brand_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Brand A')]/input")))
            brand_filter.click()
            time.sleep(2)  # Wait for UI to update
        except Exception as e:
            self.fail(f"Error during applying Brand A filter: {str(e)}")

        # Verify that number of displayed product cards changes
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".columns .products .column")
            product_count_after_filter = len(products)
            if product_count_after_filter != 1:
                self.fail("Expected product count to be 1 after applying Brand A filter")
        except Exception as e:
            self.fail(f"Error during product count verification after applying Brand A filter: {str(e)}")

        # Uncheck the "Brand A" filter
        try:
            brand_filter.click()
            time.sleep(2)  # Wait for UI to update
        except Exception as e:
            self.fail(f"Error during unchecking Brand A filter: {str(e)}")

        # Verify that the original number of product cards is restored
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".columns .products .column")
            product_count_after_unfilter = len(products)
            if product_count_after_unfilter != 2:
                self.fail("Expected product count to be 2 after unchecking Brand A filter")
        except Exception as e:
            self.fail(f"Error during product count verification after unchecking Brand A filter: {str(e)}")

        # Locate the price slider component and adjust the range
        try:
            slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .attribute-title")))
            actions = ActionChains(driver)
            handle = driver.find_element(By.CSS_SELECTOR, ".price-filter .price-filter-values .column.has-text-left")
            actions.click_and_hold(handle).move_by_offset(50, 0).release().perform()  # Adjust the offset as needed
            time.sleep(2)  # Wait for UI to update
        except Exception as e:
            self.fail(f"Error during adjusting price slider: {str(e)}")

        # Verify that the product count changes again
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".columns .products .column")
            product_count_after_price_filter = len(products)
            if product_count_after_price_filter not in [0, 1]:
                self.fail("Expected product count to change after applying price filter")
        except Exception as e:
            self.fail(f"Error during product count verification after applying price filter: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()