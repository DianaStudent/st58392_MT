import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class CategoryATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Find and click "Brand A" checkbox
        try:
            brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Brand A')]/input")))
            brand_a_checkbox.click()
            time.sleep(2)  # Wait for filter to apply
        except Exception as e:
            self.fail(f"Failed to interact with Brand A checkbox: {str(e)}")

        # Count visible products after applying Brand A filter
        try:
            products_filtered = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .available")))
            if len(products_filtered) != 1:
                self.fail("Unexpected number of products after applying Brand A filter")
        except Exception as e:
            self.fail(f"Failed to count products after Brand A filter: {str(e)}")

        # Uncheck "Brand A" checkbox
        try:
            brand_a_checkbox.click()
            time.sleep(2)  # Wait for filter to reset
        except Exception as e:
            self.fail(f"Failed to uncheck Brand A checkbox: {str(e)}")

        # Count visible products after removing Brand A filter
        try:
            products_unfiltered = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .available")))
            if len(products_unfiltered) != 2:
                self.fail("Unexpected number of products after removing Brand A filter")
        except Exception as e:
            self.fail(f"Failed to count products after removing Brand A filter: {str(e)}")

        # Move price slider and verify product count changes
        try:
            price_filter_slider = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".price-filter .column:nth-of-type(2)")))
            webdriver.ActionChains(driver).drag_and_drop_by_offset(price_filter_slider, -50, 0).perform()
            time.sleep(2)
            products_price_filtered = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .available")))
            if len(products_price_filtered) != 1:
                self.fail("Unexpected number of products after adjusting price range")
        except Exception as e:
            self.fail(f"Failed to interact with price slider: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()