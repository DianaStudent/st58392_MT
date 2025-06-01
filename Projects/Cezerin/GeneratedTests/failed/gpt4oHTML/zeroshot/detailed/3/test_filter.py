from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class FilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")  # Use a realistic URL in practice.

    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Wait until the products and filters are fully loaded
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.products .column")))
        self.assertIsNotNone(products, "Product cards did not load.")
        
        # Find and click the "Brand A" checkbox
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'attribute-title')][normalize-space()='Brand']/following-sibling::label[input[@type='checkbox' and not(@checked)]]/input")))
        self.assertIsNotNone(brand_a_checkbox, "Brand A checkbox is not present.")
        brand_a_checkbox.click()
        
        # Confirm it is checked
        time.sleep(2)  # Allow time for the filter to take effect
        self.assertTrue(brand_a_checkbox.is_selected(), "Brand A checkbox is not checked.")
        
        # Verify products are reduced
        products_after_filter = driver.find_elements(By.CSS_SELECTOR, ".columns.products .column.available")
        self.assertEqual(len(products_after_filter), 1, "Product count did not reduce as expected after Brand A filter.")
        
        # Uncheck the filter
        brand_a_checkbox.click()
        time.sleep(2)
        
        # Confirm product count is restored
        products_after_remove = driver.find_elements(By.CSS_SELECTOR, ".columns.products .column.available")
        self.assertEqual(len(products_after_remove), 2, "Product count did not restore as expected after removing Brand A filter.")
        
        # Locate and manipulate the price slider component
        price_slider_right = driver.find_element(By.CSS_SELECTOR, ".price-filter-values .column.has-text-right")
        self.assertIsNotNone(price_slider_right, "Price slider right handle is not present.")
        
        # Simulate slider movement (here we could use Actions or JS to actually drag the slider if needed)
        # This is placeholder logic due to lack of direct interaction code without specific slider library
        driver.execute_script("arguments[0].value='1159';", price_slider_right)  # Simulating adjusting maximum price
        time.sleep(2)
        
        # Verify the number of product cards is reduced
        products_after_price_filter = driver.find_elements(By.CSS_SELECTOR, ".columns.products .column.available")
        self.assertEqual(len(products_after_price_filter), 1, "Product count did not reduce as expected after price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()