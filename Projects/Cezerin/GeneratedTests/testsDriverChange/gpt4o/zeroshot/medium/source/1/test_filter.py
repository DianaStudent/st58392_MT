from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.url = "http://localhost:3000/category-a"

    def tearDown(self):
        self.driver.quit()

    def test_filters(self):
        driver = self.driver
        driver.get(self.url)

        # Wait for products to load initially
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .available"))
        )
        products_initial = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        if not products_initial:
            self.fail("Initial product list did not load.")

        initial_product_count = len(products_initial)

        # Apply "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[input[@type='checkbox'] and contains(text(), 'Brand A')]"))
        )
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify product count changes
        products_filtered = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        if not products_filtered:
            self.fail("Filtered product list did not load after applying Brand A filter.")
        
        filtered_product_count = len(products_filtered)
        self.assertNotEqual(initial_product_count, filtered_product_count, "Product count did not change after applying Brand A filter.")

        # Uncheck "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify product count is restored
        products_unfiltered = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        if not products_unfiltered:
            self.fail("Product list did not reload after unchecking Brand A filter.")
        
        unfiltered_product_count = len(products_unfiltered)
        self.assertEqual(initial_product_count, unfiltered_product_count, "Product count did not reset after unchecking Brand A filter.")

        # Locate the price slider and apply price range filter
        price_slider = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".price-filter .price-slider"))
        )
        if not price_slider:
            self.fail("Price slider did not appear.")

        # Move the price slider handle (simulated here as a single action)
        action = ActionChains(driver)
        action.click_and_hold(price_slider).move_by_offset(-30, 0).release().perform()
        time.sleep(2)

        # Verify the product count changes again
        products_price_filtered = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        if not products_price_filtered:
            self.fail("Product list did not reload after applying price filter.")

        price_filtered_product_count = len(products_price_filtered)
        self.assertNotEqual(unfiltered_product_count, price_filtered_product_count, "Product count did not change after applying price filter.")

if __name__ == "__main__":
    unittest.main()