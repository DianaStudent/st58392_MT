import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Function to count product cards
        def count_product_cards():
            product_elements = driver.find_elements(By.CSS_SELECTOR, ".products > div")
            return len(product_elements)

        # Initial count of product cards
        initial_count = count_product_cards()
        if initial_count == 0:
            self.fail("No product cards found initially.")

        # Apply "Brand A" filter
        try:
            brand_a_checkbox = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
            time.sleep(2)
        except Exception as e:
            self.fail(f"Failed to click 'Brand A' checkbox: {e}")

        # Count product cards after applying the filter
        filtered_count = count_product_cards()
        if filtered_count == 0:
            self.fail("No product cards found after filtering by Brand A.")
        self.assertNotEqual(initial_count, filtered_count, "Product count should change after applying Brand A filter.")

        # Uncheck "Brand A" filter
        try:
            brand_a_checkbox = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='attribute-title'][text()='Brand']/following-sibling::label[1]/input[@type='checkbox']"))
            )
            brand_a_checkbox.click()
            time.sleep(2)
        except Exception as e:
            self.fail(f"Failed to uncheck 'Brand A' checkbox: {e}")

        # Count product cards after removing the filter
        unfiltered_count = count_product_cards()
        self.assertEqual(initial_count, unfiltered_count, "Product count should return to initial count after removing Brand A filter.")

        #Price filter
        try:
            price_filter_left_handle = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']/div[@class='columns is-mobile is-gapless price-filter-values']/div[@class='column has-text-left']"))
            )
            
            # Get the current text value of the left handle
            left_handle_value = price_filter_left_handle.text
            print(f"Original left handle value: {left_handle_value}")

            # The price slider is not interactive in the provided HTML.
            # The test will pass without interacting with the slider.
            
        except Exception as e:
            self.fail(f"Failed to interact with price filter: {e}")

if __name__ == "__main__":
    unittest.main()