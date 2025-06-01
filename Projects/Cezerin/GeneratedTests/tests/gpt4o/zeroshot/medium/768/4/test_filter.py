import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver

        # Verify initial products count
        initial_products = driver.find_elements(By.CSS_SELECTOR, "div.products > div.available")
        self.assertTrue(len(initial_products) > 0, "Initial product list is empty")

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = driver.find_element(By.XPATH, "//label[text()='Brand A']/input")
        self.assertIsNotNone(brand_a_checkbox, "Brand A checkbox is missing")
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify the number of displayed product cards changes
        filtered_products = driver.find_elements(By.CSS_SELECTOR, "div.products > div.available")
        self.assertNotEqual(len(initial_products), len(filtered_products), "Product count did not change after applying Brand A filter")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        time.sleep(2)

        # Verify the original number of product cards is restored
        restored_products = driver.find_elements(By.CSS_SELECTOR, "div.products > div.available")
        self.assertEqual(len(initial_products), len(restored_products), "Product count did not restore after removing Brand A filter")

        # Locate the price slider and adjust it to change the price filter
        price_slider = driver.find_element(By.CSS_SELECTOR, ".price-filter .price-filter-values")
        self.assertIsNotNone(price_slider, "Price slider component is missing")
        
        actions = ActionChains(driver)
        slider_handle = driver.find_element(By.CSS_SELECTOR, ".price-filter .column.has-text-left")
        actions.click_and_hold(slider_handle).move_by_offset(50, 0).release().perform()
        time.sleep(2)

        # Verify the product count changes again
        post_price_filter_products = driver.find_elements(By.CSS_SELECTOR, "div.products > div.available")
        self.assertNotEqual(len(restored_products), len(post_price_filter_products), "Product count did not change after applying price filter")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()