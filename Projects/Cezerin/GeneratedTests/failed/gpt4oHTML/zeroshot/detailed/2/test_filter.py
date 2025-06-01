from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver: WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        
        # Navigate to the Category A page
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_brand_a_filter_and_price_slider(self):
        driver = self.driver
        
        # 2. Wait for products and filters to be fully loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".attribute-filter"))
        )
        
        # Check initial product count
        initial_products = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .available"))
        )
        initial_product_count = len(initial_products)
        if initial_product_count == 0:
            self.fail("No initial products found")
        
        # 3. Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Brand A']/input"))
        )
        brand_a_checkbox.click()

        # 4. Confirm it is checked
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox is not checked after clicking.")
        
        # Wait for filtering results
        time.sleep(2)

        # 5. Verify that the number of product cards is reduced
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        filtered_product_count = len(filtered_products)
        self.assertLess(filtered_product_count, initial_product_count, "Product count did not reduce after applying filter")

        # 6. Uncheck the filter and confirm product count is restored
        brand_a_checkbox.click()
        time.sleep(2)
        
        restored_products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        restored_product_count = len(restored_products)
        self.assertEqual(restored_product_count, initial_product_count, "Product count did not restore after unchecking filter")

        # 7. Locate the price slider component and move the right slider handle
        # Assumes the presence of an input[type=range] as the slider
        price_slider = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[role='slider']"))
        )

        # Confirm initial slider values
        aria_max = price_slider.get_attribute("aria-valuemax")
        self.assertIsNotNone(aria_max, "Slider max value is missing")
        
        # Move the slider to reduce the maximum price to 1159
        driver.execute_script("arguments[0].setAttribute('aria-valuenow', 1159)", price_slider)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", price_slider)

        # Wait for filtering results
        time.sleep(2)

        # 9. Verify that the number of product cards is reduced
        price_filtered_products = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        price_filtered_product_count = len(price_filtered_products)
        self.assertLess(price_filtered_product_count, initial_product_count, "Product count did not reduce after adjusting the price slider")

if __name__ == "__main__":
    unittest.main()