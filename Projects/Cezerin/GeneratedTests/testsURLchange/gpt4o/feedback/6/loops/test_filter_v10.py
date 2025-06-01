import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/category-a')
    
    def test_product_filter(self):
        driver = self.driver

        # Wait and verify initial number of products
        product_cards = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .column.available"))
        )
        initial_count = len(product_cards)
        if initial_count == 0:
            self.fail("No products found initially.")

        # Apply "Brand A" filter
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Brand')]/following-sibling::label/input[@type='checkbox' and contains(following-sibling::text(), 'Brand A')]"))
        )
        brand_a_checkbox.click()

        # Wait for UI to update
        time.sleep(2)

        # Verify product count changes after applying filter
        filtered_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .column.available")
        filtered_count = len(filtered_products)
        if filtered_count == initial_count:
            self.fail("Product count did not change after applying Brand A filter.")

        # Uncheck "Brand A" filter
        brand_a_checkbox.click()

        # Wait for UI to update
        time.sleep(2)

        # Verify original product count is restored
        restored_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .column.available")
        restored_count = len(restored_products)
        if restored_count != initial_count:
            self.fail("Product count did not restore after removing Brand A filter.")

        # Locate the price filter
        price_filter_div = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .price-filter-values"))
        )
        
        # Perform action to move the price slider
        slider_handle = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='price-filter']//div[@class='column has-text-left']"))
        )
        ActionChains(driver).click_and_hold(slider_handle).move_by_offset(-50, 0).release().perform()

        # Wait for UI to update
        time.sleep(2)

        # Verify product count changes again after adjusting price filter
        price_filtered_products = driver.find_elements(By.CSS_SELECTOR, ".columns.is-multiline.is-mobile.products .column.available")
        final_count = len(price_filtered_products)
        if final_count == restored_count:
            self.fail("Product count did not change after adjusting the price filter.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()