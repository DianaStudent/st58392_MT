from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()
    
    def test_product_filter(self):
        driver = self.driver

        try:
            # Wait and find "Brand A" filter checkbox
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//label[input[@value='Brand A']]"))
            )
            brand_a_checkbox.click()

            # Wait 2 seconds
            time.sleep(2)

            # Check number of products after applying "Brand A" filter
            products_after_brand_filter = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available"))
            self.assertEqual(products_after_brand_filter, 1, "Product count should be 1 after filtering by Brand A")

            # Uncheck "Brand A" filter
            brand_a_checkbox.click()

            # Wait 2 seconds
            time.sleep(2)

            # Check number of products after removing "Brand A" filter
            products_after_removing_brand_filter = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available"))
            self.assertEqual(products_after_removing_brand_filter, 2, "Product count should be 2 after removing Brand A filter")

            # Interact with the price slider
            # Note: Assuming a slider element with manageable interaction points. 
            # This might need libraries like ActionChains for complex interactions.
            price_slider = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price-filter"))
            )
            ActionChains(driver).drag_and_drop_by_offset(price_slider, -50, 0).perform()

            # Wait 2 seconds
            time.sleep(2)

            # Check number of products after changing price range
            products_after_price_filter = len(driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .available"))
            self.assertEqual(products_after_price_filter, 1, "Product count should be 1 after modifying the price filter")

        except Exception as e:
            self.fail(f"Test failed due to missing element or error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()